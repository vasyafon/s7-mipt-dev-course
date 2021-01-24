from typing import Iterable, Tuple
import asyncpg
from asyncpg.pool import Pool
import os
import asyncio

DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'None')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5666')
DB_NAME = os.getenv('DB_NAME', 'disruption')
DB_SCHEMA = os.getenv('DB_SCHEMA', 'current')


class PgPool(object):
    _pool: Pool = None
    pool_initializing = False

    @classmethod
    async def get_pool(cls) -> Pool:
        if not cls.pool_initializing and (cls._pool is None or cls._pool._loop._closed):
            cls.pool_initializing = True
            print("Creating new pool")
            cls._pool = await asyncpg.create_pool(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD,
                database=DB_NAME, max_inactive_connection_lifetime=60)
            cls.pool_initializing = False
        elif cls.pool_initializing:
            while cls.pool_initializing:
                await asyncio.sleep(0.1)

        return cls._pool


async def execute_queries(queries_and_args: Iterable[Tuple[str, Iterable[Iterable]]]):
    pool = await PgPool.get_pool()
    async with pool.acquire() as conn:
        async with conn.transaction():
            for query, args in queries_and_args:
                result = await conn.execute(query, *args)
    return result


async def abstract_query(command, query, args=(), pool: Pool = None):
    pool = await PgPool.get_pool()
    async with pool.acquire() as conn:
        async with conn.transaction():
            func = getattr(conn, command)
            result = await func(query, *args)
    return result


async def execute_query(query, args=(), pool: Pool = None):
    return await abstract_query('execute', query, args, pool)


async def fetch_all_query(query, args=(), pool: Pool = None):
    return await abstract_query('fetch', query, args, pool)


async def fetch_one_query(query, args=(), pool: Pool = None):
    return await abstract_query('fetchrow', query, args, pool)
