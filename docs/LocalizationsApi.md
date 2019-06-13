# dyspatch_client.LocalizationsApi

All URIs are relative to *https://api.dyspatch.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**localizations_localization_id_get**](LocalizationsApi.md#localizations_localization_id_get) | **GET** /localizations/{localizationId} | Get Localization Object by ID

# **localizations_localization_id_get**
> LocalizationRead localizations_localization_id_get(localization_id, target_language=target_language)

Get Localization Object by ID

Returns a specific localization object with a matching ID

### Example
```python
from __future__ import print_function
import time
import dyspatch_client
from dyspatch_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Bearer
configuration = dyspatch_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = dyspatch_client.LocalizationsApi(dyspatch_client.ApiClient(configuration))
localization_id = 'localization_id_example' # str | A localization ID
target_language = 'target_language_example' # str | The type of templating language to compile as. Should only be used for visual templates. (optional)

try:
    # Get Localization Object by ID
    api_response = api_instance.localizations_localization_id_get(localization_id, target_language=target_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocalizationsApi->localizations_localization_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **localization_id** | **str**| A localization ID | 
 **target_language** | **str**| The type of templating language to compile as. Should only be used for visual templates. | [optional] 

### Return type

[**LocalizationRead**](LocalizationRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2019.03+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

