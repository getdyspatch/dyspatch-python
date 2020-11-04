# dyspatch_client.LocalizationsApi

All URIs are relative to *https://api.dyspatch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_localization_by_id**](LocalizationsApi.md#get_localization_by_id) | **GET** /localizations/{localizationId} | Get Localization Object by ID


# **get_localization_by_id**
> LocalizationRead get_localization_by_id(localization_id, target_language, accept)

Get Localization Object by ID

Returns a specific localization object with a matching ID

### Example

* Api Key Authentication (Bearer):
```python
from __future__ import print_function
import time
import dyspatch_client
from dyspatch_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.dyspatch.io
# See configuration.py for a list of all supported configuration parameters.
configuration = dyspatch_client.Configuration(
    host = "https://api.dyspatch.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration = dyspatch_client.Configuration(
    host = "https://api.dyspatch.io",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with dyspatch_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dyspatch_client.LocalizationsApi(api_client)
    localization_id = 'localization_id_example' # str | A localization ID
target_language = 'target_language_example' # str | The type of templating language to compile as. Should only be used for visual templates.
accept = 'accept_example' # str | A version of the API that should be used for the request. For example, to use version \"2020.08\", set the value to \"application/vnd.dyspatch.2020.08+json\"

    try:
        # Get Localization Object by ID
        api_response = api_instance.get_localization_by_id(localization_id, target_language, accept)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LocalizationsApi->get_localization_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **localization_id** | **str**| A localization ID | 
 **target_language** | **str**| The type of templating language to compile as. Should only be used for visual templates. | 
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.08\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.08+json\&quot; | 

### Return type

[**LocalizationRead**](LocalizationRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2020.08+json, */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A localization object with the requested ID |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**400** | Invalid request |  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
**401** | Unauthenticated |  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
**403** | Unauthorized |  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
**404** | Resource not found |  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
**429** | Rate limit exceeded |  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
**500** | Server error |  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |
**0** | Server error |  * X-RateLimit-Remaining - The number of requests left for the time window. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

