# auth_python_client.AuthApi

All URIs are relative to *http://localhost:8080/api/auth/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_google**](AuthApi.md#auth_google) | **GET** /authGoogle | Authenticate on Google
[**get_public_key**](AuthApi.md#get_public_key) | **GET** /publicKey | get public key to decrypt access tokens
[**get_user_info**](AuthApi.md#get_user_info) | **GET** /userInfo | get user information
[**login**](AuthApi.md#login) | **POST** /login | Authenticate on OpenID
[**open_google_auth**](AuthApi.md#open_google_auth) | **GET** /loginGoogle | Redirect to Google Authentication
[**refresh**](AuthApi.md#refresh) | **POST** /refresh | generate access token from refresh token


# **auth_google**
> Tokens auth_google()

Authenticate on Google

### Example

```python
import time
import auth_python_client
from auth_python_client.api import auth_api
from auth_python_client.model.tokens import Tokens
from auth_python_client.model.api_error import ApiError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_python_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)


# Enter a context with an instance of the API client
with auth_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    state = "state_example" # str |  (optional)
    code = "code_example" # str |  (optional)
    scope = "scope_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authenticate on Google
        api_response = api_instance.auth_google(state=state, code=code, scope=scope)
        pprint(api_response)
    except auth_python_client.ApiException as e:
        print("Exception when calling AuthApi->auth_google: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**|  | [optional]
 **code** | **str**|  | [optional]
 **scope** | **str**|  | [optional]

### Return type

[**Tokens**](Tokens.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User tokens |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_key**
> PublicKey get_public_key()

get public key to decrypt access tokens

### Example

```python
import time
import auth_python_client
from auth_python_client.api import auth_api
from auth_python_client.model.public_key import PublicKey
from auth_python_client.model.api_error import ApiError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_python_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)


# Enter a context with an instance of the API client
with auth_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get public key to decrypt access tokens
        api_response = api_instance.get_public_key()
        pprint(api_response)
    except auth_python_client.ApiException as e:
        print("Exception when calling AuthApi->get_public_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicKey**](PublicKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Public key |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_info**
> UserInfo get_user_info()

get user information

### Example

* Bearer Authentication (BearerAuth):
```python
import time
import auth_python_client
from auth_python_client.api import auth_api
from auth_python_client.model.user_info import UserInfo
from auth_python_client.model.api_error import ApiError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_python_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = auth_python_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # get user information
        api_response = api_instance.get_user_info()
        pprint(api_response)
    except auth_python_client.ApiException as e:
        print("Exception when calling AuthApi->get_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**200** | User information |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> Tokens login(login_credentials)

Authenticate on OpenID

### Example

```python
import time
import auth_python_client
from auth_python_client.api import auth_api
from auth_python_client.model.tokens import Tokens
from auth_python_client.model.login_credentials import LoginCredentials
from auth_python_client.model.api_error import ApiError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_python_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)


# Enter a context with an instance of the API client
with auth_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    login_credentials = LoginCredentials(
        code="code_example",
        code_verifier="code_verifier_example",
        nonce="nonce_example",
        redirect_uri="redirect_uri_example",
    ) # LoginCredentials | 

    # example passing only required values which don't have defaults set
    try:
        # Authenticate on OpenID
        api_response = api_instance.login(login_credentials)
        pprint(api_response)
    except auth_python_client.ApiException as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_credentials** | [**LoginCredentials**](LoginCredentials.md)|  |

### Return type

[**Tokens**](Tokens.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User tokens |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_google_auth**
> open_google_auth()

Redirect to Google Authentication

### Example

```python
import time
import auth_python_client
from auth_python_client.api import auth_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_python_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)


# Enter a context with an instance of the API client
with auth_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Redirect to Google Authentication
        api_instance.open_google_auth()
    except auth_python_client.ApiException as e:
        print("Exception when calling AuthApi->open_google_auth: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirection to Google |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh**
> TokenResponse refresh()

generate access token from refresh token

### Example

* Bearer Authentication (RefreshAuth):
```python
import time
import auth_python_client
from auth_python_client.api import auth_api
from auth_python_client.model.token_response import TokenResponse
from auth_python_client.model.api_error import ApiError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_python_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: RefreshAuth
configuration = auth_python_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with auth_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # generate access token from refresh token
        api_response = api_instance.refresh()
        pprint(api_response)
    except auth_python_client.ApiException as e:
        print("Exception when calling AuthApi->refresh: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[RefreshAuth](../README.md#RefreshAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Access token |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

