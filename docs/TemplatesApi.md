# dyspatch_client.TemplatesApi

All URIs are relative to *https://api.dyspatch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_template_by_id**](TemplatesApi.md#get_template_by_id) | **GET** /templates/{templateId} | Get Template by ID
[**get_templates**](TemplatesApi.md#get_templates) | **GET** /templates | List Templates


# **get_template_by_id**
> TemplateRead get_template_by_id(template_id, target_language, accept)

Get Template by ID

Gets a template object with the matching ID. If the template has published content the \"compiled\" field will contain the template .

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import templates_api
from dyspatch_client.model.api_error import APIError
from dyspatch_client.model.template_read import TemplateRead
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
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with dyspatch_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    template_id = "templateId_example" # str | A template ID
    target_language = "html" # str | The type of templating language to compile as. Should only be used for visual templates.
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"

    # example passing only required values which don't have defaults set
    try:
        # Get Template by ID
        api_response = api_instance.get_template_by_id(template_id, target_language, accept)
        pprint(api_response)
    except dyspatch_client.ApiException as e:
        print("Exception when calling TemplatesApi->get_template_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| A template ID |
 **target_language** | **str**| The type of templating language to compile as. Should only be used for visual templates. |
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |

### Return type

[**TemplateRead**](TemplateRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2020.11+json, */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A template object with the requested ID. If the template has no published content the \&quot;compiled\&quot; field will be *null*. |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**400** | Invalid request |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**401** | Unauthenticated |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**403** | Unauthorized |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**404** | Resource not found |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**429** | Rate limit exceeded |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**500** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**0** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_templates**
> TemplatesRead get_templates(accept)

List Templates

Gets a list of Template Metadata objects for all templates. Up to 25 results returned before results are paginated.

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import templates_api
from dyspatch_client.model.templates_read import TemplatesRead
from dyspatch_client.model.api_error import APIError
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
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with dyspatch_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = templates_api.TemplatesApi(api_client)
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"
    cursor = "cursor_example" # str | A cursor value used to retrieve a specific page from a paginated result set. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Templates
        api_response = api_instance.get_templates(accept)
        pprint(api_response)
    except dyspatch_client.ApiException as e:
        print("Exception when calling TemplatesApi->get_templates: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Templates
        api_response = api_instance.get_templates(accept, cursor=cursor)
        pprint(api_response)
    except dyspatch_client.ApiException as e:
        print("Exception when calling TemplatesApi->get_templates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |
 **cursor** | **str**| A cursor value used to retrieve a specific page from a paginated result set. | [optional]

### Return type

[**TemplatesRead**](TemplatesRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2020.11+json, */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of templates |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**400** | Invalid request |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**401** | Unauthenticated |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**403** | Unauthorized |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**429** | Rate limit exceeded |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**500** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**0** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

