# swagger_client.TemplatesApi

All URIs are relative to *https://api.dyspatch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**templates_get**](TemplatesApi.md#templates_get) | **GET** /templates | List Templates
[**templates_template_id_drafts_get**](TemplatesApi.md#templates_template_id_drafts_get) | **GET** /templates/{templateId}/drafts | List Template Drafts
[**templates_template_id_drafts_template_draft_id_get**](TemplatesApi.md#templates_template_id_drafts_template_draft_id_get) | **GET** /templates/{templateId}/drafts/{templateDraftId} | Get a Draft
[**templates_template_id_get**](TemplatesApi.md#templates_template_id_get) | **GET** /templates/{templateId} | Get Template by ID


# **templates_get**
> TemplatesRead templates_get(cursor=cursor)

List Templates

Gets a list of Template Metadata objects for all templates. Up to 25 results returned before results are paginated.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
cursor = 'cursor_example' # str | A cursor value used to retrieve a specific page from a paginated result set. (optional)

try:
    # List Templates
    api_response = api_instance.templates_get(cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| A cursor value used to retrieve a specific page from a paginated result set. | [optional] 

### Return type

[**TemplatesRead**](TemplatesRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2018.02+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_template_id_drafts_get**
> TemplateDraftsRead templates_template_id_drafts_get(template_id, cursor=cursor)

List Template Drafts

Gets a list of Template Draft Metadata objects for the specified template. Up to 25 results returned before results are paginated. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | A template ID
cursor = 'cursor_example' # str | A cursor value used to retrieve a specific page from a paginated result set. (optional)

try:
    # List Template Drafts
    api_response = api_instance.templates_template_id_drafts_get(template_id, cursor=cursor)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_template_id_drafts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| A template ID | 
 **cursor** | **str**| A cursor value used to retrieve a specific page from a paginated result set. | [optional] 

### Return type

[**TemplateDraftsRead**](TemplateDraftsRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2018.02+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_template_id_drafts_template_draft_id_get**
> TemplateDraftRead templates_template_id_drafts_template_draft_id_get(template_draft_id, template_id)

Get a Draft

Gets a Draft object of a Template. This endpoint provides access to unpublished Template drafts. Note that accessing invalid template drafts 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
template_draft_id = 'template_draft_id_example' # str | A draft ID
template_id = 'template_id_example' # str | A template ID

try:
    # Get a Draft
    api_response = api_instance.templates_template_id_drafts_template_draft_id_get(template_draft_id, template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_template_id_drafts_template_draft_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_draft_id** | **str**| A draft ID | 
 **template_id** | **str**| A template ID | 

### Return type

[**TemplateDraftRead**](TemplateDraftRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2018.02+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **templates_template_id_get**
> TemplateRead templates_template_id_get(template_id)

Get Template by ID

Gets a template object with the matching ID. If the template has published content the \"compiled\" field will contain the template .

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TemplatesApi(swagger_client.ApiClient(configuration))
template_id = 'template_id_example' # str | A template ID

try:
    # Get Template by ID
    api_response = api_instance.templates_template_id_get(template_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TemplatesApi->templates_template_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| A template ID | 

### Return type

[**TemplateRead**](TemplateRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2018.02+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

