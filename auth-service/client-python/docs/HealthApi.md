# auth_python_client.HealthApi

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
import time
import auth_python_client
from auth_python_client.api import health_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_python_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)


# Enter a context with an instance of the API client
with auth_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # liveness probe
        api_instance.health_liveness_get()
    except auth_python_client.ApiException as e:
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
import time
import auth_python_client
from auth_python_client.api import health_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:8080/api/auth/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = auth_python_client.Configuration(
    host = "http://localhost:8080/api/auth/v1"
)


# Enter a context with an instance of the API client
with auth_python_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = health_api.HealthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # readiness probe
        api_instance.health_readiness_get()
    except auth_python_client.ApiException as e:
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

