import asyncio
from aiohttp import ClientError


async def retry_call(func, args=(), kwargs=None, api_exception=None):
    retries = 0
    result = None
    while True:
        exceptions = [asyncio.TimeoutError, ClientError]
        if api_exception is not None:
            exceptions.append(api_exception)
        try:
            if kwargs is None:
                kwargs = {}
            result = await func(*args, **kwargs)
            break
        except exceptions as ex:
            if isinstance(ex, api_exception):
                print(f"Exception {retries}: ", str(ex.status))
                if ex.status in (400, 401, 402, 403):
                    raise ex
            else:
                print(f"Exception {retries}: ", str(ex))
            retries += 1
            if retries > 3:
                raise ex
            await asyncio.sleep(1 + retries ** 2)
            continue
    return result
