# swagger_client.LocalizationsApi

All URIs are relative to *https://api.dyspatch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**localizations_localization_id_drafts_template_draft_id_get**](LocalizationsApi.md#localizations_localization_id_drafts_template_draft_id_get) | **GET** /localizations/{localizationId}/drafts/{templateDraftId} | Gets a Localized Draft
[**localizations_localization_id_get**](LocalizationsApi.md#localizations_localization_id_get) | **GET** /localizations/{localizationId} | Get Localization Object by ID


# **localizations_localization_id_drafts_template_draft_id_get**
> LocalizationDraftRead localizations_localization_id_drafts_template_draft_id_get(template_draft_id, localization_id)

Gets a Localized Draft

Returns a localized Draft object

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
api_instance = swagger_client.LocalizationsApi(swagger_client.ApiClient(configuration))
template_draft_id = 'template_draft_id_example' # str | A draft ID
localization_id = 'localization_id_example' # str | A localization ID

try:
    # Gets a Localized Draft
    api_response = api_instance.localizations_localization_id_drafts_template_draft_id_get(template_draft_id, localization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationsApi->localizations_localization_id_drafts_template_draft_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_draft_id** | **str**| A draft ID | 
 **localization_id** | **str**| A localization ID | 

### Return type

[**LocalizationDraftRead**](LocalizationDraftRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2018.02+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **localizations_localization_id_get**
> LocalizationRead localizations_localization_id_get(localization_id)

Get Localization Object by ID

Returns a specific localization object with a matching ID

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
api_instance = swagger_client.LocalizationsApi(swagger_client.ApiClient(configuration))
localization_id = 'localization_id_example' # str | A localization ID

try:
    # Get Localization Object by ID
    api_response = api_instance.localizations_localization_id_get(localization_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationsApi->localizations_localization_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **localization_id** | **str**| A localization ID | 

### Return type

[**LocalizationRead**](LocalizationRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2018.02+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

