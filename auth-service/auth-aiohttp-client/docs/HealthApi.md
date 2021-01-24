# auth_aiohttp_client.HealthApi

All URIs are relative to *http://localhost:8080/api/auth/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_liveness_get**](HealthApi.md#health_liveness_get) | **GET** /health/liveness | liveness probe
[**health_readiness_get**](HealthApi.md#health_readiness_get) | **GET** /health/readiness | readiness probe


# **health_liveness_get**
> health_liveness_get()

liveness probe

### Example

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


# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.HealthApi(api_client)
    
    try:
        # liveness probe
        api_instance.health_liveness_get()
    except ApiException as e:
        print("Exception when calling HealthApi->health_liveness_get: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_readiness_get**
> health_readiness_get()

readiness probe

### Example

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


# Enter a context with an instance of the API client
with auth_aiohttp_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_aiohttp_client.HealthApi(api_client)
    
    try:
        # readiness probe
        api_instance.health_readiness_get()
    except ApiException as e:
        print("Exception when calling HealthApi->health_readiness_get: %s\n" % e)
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

