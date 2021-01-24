# auth_aiohttp_client.AdminApi

All URIs are relative to *http://localhost:8080/api/auth/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_add_group**](AdminApi.md#admin_add_group) | **POST** /admin/groups | add new group
[**admin_add_user**](AdminApi.md#admin_add_user) | **POST** /admin/users | add new user
[**admin_get_group**](AdminApi.md#admin_get_group) | **GET** /admin/groups/{groupId} | Get group
[**admin_get_user_info**](AdminApi.md#admin_get_user_info) | **GET** /admin/users/{userId} | Get user info
[**admin_group_put**](AdminApi.md#admin_group_put) | **PUT** /admin/groups/{groupId} | Edit group
[**admin_list_groups**](AdminApi.md#admin_list_groups) | **GET** /admin/groups | list all groups
[**admin_list_users**](AdminApi.md#admin_list_users) | **GET** /admin/users | list all users
[**admin_remove_group**](AdminApi.md#admin_remove_group) | **DELETE** /admin/groups/{groupId} | Remove group from the system
[**admin_remove_user**](AdminApi.md#admin_remove_user) | **DELETE** /admin/users/{userId} | Remove user from the system
[**admin_user_put**](AdminApi.md#admin_user_put) | **PUT** /admin/users/{userId} | Edit user
[**generate_refresh_token**](AdminApi.md#generate_refresh_token) | **POST** /admin/refreshTokens | generate refresh token with arbitrary lifetime e.g. for services
[**get_token_info**](AdminApi.md#get_token_info) | **GET** /admin/refreshTokens/{tokenId} | list all refresh tokens
[**list_refresh_tokens**](AdminApi.md#list_refresh_tokens) | **GET** /admin/refreshTokens | list all refresh tokens
[**revoke_refresh_token**](AdminApi.md#revoke_refresh_token) | **DELETE** /admin/refreshTokens/{tokenId} | generate refresh token with arbitrary lifetime e.g. for services


# **admin_add_group**
> GroupFull admin_add_group(group_post)

add new group

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    group_post = auth_aiohttp_client.GroupPost() # GroupPost | User parameters

    try:
        # add new group
        api_response = api_instance.admin_add_group(group_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_add_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_post** | [**GroupPost**](GroupPost.md)| User parameters | 

### Return type

[**GroupFull**](GroupFull.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_add_user**
> UserInfo admin_add_user(user_info)

add new user

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    user_info = auth_aiohttp_client.UserInfo() # UserInfo | User parameters

    try:
        # add new user
        api_response = api_instance.admin_add_user(user_info)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_add_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_info** | [**UserInfo**](UserInfo.md)| User parameters | 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_group**
> GroupFull admin_get_group(group_id)

Get group

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    group_id = 'group_id_example' # str | 

    try:
        # Get group
        api_response = api_instance.admin_get_group(group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

[**GroupFull**](GroupFull.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_get_user_info**
> UserInfo admin_get_user_info(user_id)

Get user info

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get user info
        api_response = api_instance.admin_get_user_info(user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_get_user_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_group_put**
> GroupFull admin_group_put(group_id, group_full)

Edit group

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    group_id = 'group_id_example' # str | 
group_full = auth_aiohttp_client.GroupFull() # GroupFull | User parameters

    try:
        # Edit group
        api_response = api_instance.admin_group_put(group_id, group_full)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_group_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **group_full** | [**GroupFull**](GroupFull.md)| User parameters | 

### Return type

[**GroupFull**](GroupFull.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_list_groups**
> GroupList admin_list_groups()

list all groups

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    
    try:
        # list all groups
        api_response = api_instance.admin_list_groups()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_list_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupList**](GroupList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups list |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_list_users**
> UserInfoList admin_list_users()

list all users

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    
    try:
        # list all users
        api_response = api_instance.admin_list_users()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_list_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfoList**](UserInfoList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users list |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_remove_group**
> admin_remove_group(group_id)

Remove group from the system

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    group_id = 'group_id_example' # str | 

    try:
        # Remove group from the system
        api_instance.admin_remove_group(group_id)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_remove_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_remove_user**
> admin_remove_user(user_id)

Remove user from the system

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Remove user from the system
        api_instance.admin_remove_user(user_id)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_remove_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **admin_user_put**
> UserInfo admin_user_put(user_id, user_info)

Edit user

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    user_id = 'user_id_example' # str | 
user_info = auth_aiohttp_client.UserInfo() # UserInfo | User parameters

    try:
        # Edit user
        api_response = api_instance.admin_user_put(user_id, user_info)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->admin_user_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **user_info** | [**UserInfo**](UserInfo.md)| User parameters | 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Info |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_refresh_token**
> Tokens generate_refresh_token(admin_refresh_token_info_post)

generate refresh token with arbitrary lifetime e.g. for services

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    admin_refresh_token_info_post = auth_aiohttp_client.AdminRefreshTokenInfoPost() # AdminRefreshTokenInfoPost | Token setup

    try:
        # generate refresh token with arbitrary lifetime e.g. for services
        api_response = api_instance.generate_refresh_token(admin_refresh_token_info_post)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->generate_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_refresh_token_info_post** | [**AdminRefreshTokenInfoPost**](AdminRefreshTokenInfoPost.md)| Token setup | 

### Return type

[**Tokens**](Tokens.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Tokens |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_info**
> AdminRefreshTokenInfo get_token_info(token_id)

list all refresh tokens

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    token_id = 'token_id_example' # str | 

    try:
        # list all refresh tokens
        api_response = api_instance.get_token_info(token_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->get_token_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 

### Return type

[**AdminRefreshTokenInfo**](AdminRefreshTokenInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refresh tokens list |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_refresh_tokens**
> AdminRefreshTokenList list_refresh_tokens()

list all refresh tokens

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    
    try:
        # list all refresh tokens
        api_response = api_instance.list_refresh_tokens()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->list_refresh_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminRefreshTokenList**](AdminRefreshTokenList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Refresh tokens list |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_refresh_token**
> revoke_refresh_token(token_id)

generate refresh token with arbitrary lifetime e.g. for services

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import auth_aiohttp_client
from auth_aiohttp_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_aiohttp_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_aiohttp_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.AdminApi(api_client)
    token_id = 'token_id_example' # str | 

    try:
        # generate refresh token with arbitrary lifetime e.g. for services
        api_instance.revoke_refresh_token(token_id)
    except ApiException as e:
        print("Exception when calling AdminApi->revoke_refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

