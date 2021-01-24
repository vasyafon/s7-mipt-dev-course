from contextlib import closing
from typing import Iterable, Tuple

import asyncpg
from asyncpg.pool import Pool
from flask import g, app
import os
import asyncio
from auth_server.const import Const


class PgPool(object):
    _pool: Pool = None
    pool_initializing = False

    @classmethod
    async def get_pool(cls) -> Pool:
        if not cls.pool_initializing and (cls._pool is None or cls._pool._loop._closed):
            cls.pool_initializing = True
            print("Creating new pool")
            cls._pool = await asyncpg.create_pool(host=Const.DB_HOST,
                                                  port=Const.DB_PORT,
                                                  user=Const.DB_USER,
                                                  password=Const.DB_PASSWORD,
                                                  database=Const.DB_NAME,
                                                  max_inactive_connection_lifetime=60)
            cls.pool_initializing = False
        elif cls.pool_initializing:
            while cls.pool_initializing:
                await asyncio.sleep(0.1)

        return cls._pool


# def get_db_connection():
#     return connect(
#         f'dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}')


# def get_db():
#     if 'db' not in g:
#         g.db = connect(
#             f'dbname={DB_NAME} user={DB_USER} password={DB_PASSWORD} host={DB_HOST} port={DB_PORT}')
#     return g.db


# def execute_query(query, vars=None):
#     conn = get_db()
#     cursor = conn.cursor()
#     cursor.execute(query, vars=vars)
#     conn.commit()
#
async def execute_queries(queries_and_args: Iterable[Tuple[str, Iterable[Iterable]]]):
    # conn = await PgPool.get_conn()
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
