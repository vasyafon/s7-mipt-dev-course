from airport_load_server.functions.global_info import get_global_load


async def test_global_load():
    await get_global_load()