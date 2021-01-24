import os
from typing import Optional

from mipt_auth_wrapper.token_info import TokenInfo, AuthMethod

class DsmApiClient:
    """
    How to use ?

    api_key = get_session_str()
    async with DsmApiClient(
            dsm_info_aiohttp_client,
            dsm_info_aiohttp_client.HealthApi,
            info_url,
            api_key) as c:
        print(c.health_liveness_get())
    """

    def __init__(self, module, api, api_url, api_key=None, token_info: Optional[TokenInfo] = None):
        config = module.Configuration(
            host=api_url,

        )
        config.access_token = None

        if token_info is None or token_info.auth_method == AuthMethod.cookie:
            if api_key is None:
                token_info: TokenInfo
                api_key = token_info.api_key
            config.api_key = {'CookieAuth': 'session'},
            config.api_key_prefix = {'CookieAuth': 'session'}
            client = module.ApiClient(configuration=config, cookie=f'session={api_key}')
        else:
            config.access_token = token_info.api_key
            client = module.ApiClient(configuration=config)

        self.api = api(client)

    async def __aenter__(self):
        return self.api

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.api.api_client.close()
