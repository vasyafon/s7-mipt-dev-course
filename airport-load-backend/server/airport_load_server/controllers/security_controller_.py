from typing import List, Optional

from mipt_auth_wrapper import decode_api_key_v2, TokenInfo

from airport_load_server.functions.const import Const


def info_from_BearerAuth(token: str) -> Optional[TokenInfo]:
    """
    Check and retrieve authentication information from custom bearer token.
    Returned value will be passed in 'token_info' parameter of your operation function, if there is one.
    'sub' or 'uid' will be set in 'user' parameter of your operation function, if there is one.
    Should return None if auth is invalid or does not allow access to called API.
    """
    return decode_api_key_v2(token, Const.AUTH_PUBLIC_KEY)
