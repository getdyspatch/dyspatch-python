# dyspatch_client.DraftsApi

All URIs are relative to *https://api.dyspatch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_localization**](DraftsApi.md#delete_localization) | **DELETE** /drafts/{draftId}/localizations/{languageId} | Remove a localization
[**get_draft_by_id**](DraftsApi.md#get_draft_by_id) | **GET** /drafts/{draftId} | Get Draft by ID
[**get_draft_localization_keys**](DraftsApi.md#get_draft_localization_keys) | **GET** /drafts/{draftId}/localizationKeys | Get localization keys
[**get_drafts**](DraftsApi.md#get_drafts) | **GET** /drafts | List Drafts
[**get_localization_for_draft**](DraftsApi.md#get_localization_for_draft) | **GET** /drafts/{draftId}/localizations | Get localizations on a draft
[**save_localization**](DraftsApi.md#save_localization) | **PUT** /drafts/{draftId}/localizations/{languageId} | Create or update a localization
[**set_translation**](DraftsApi.md#set_translation) | **PUT** /drafts/{draftId}/localizations/{languageId}/translations | Set translations for language
[**submit_draft_for_approval**](DraftsApi.md#submit_draft_for_approval) | **POST** /drafts/{draftId}/publishRequest | Submit the draft for approval


# **delete_localization**
> delete_localization(draft_id, language_id, accept)

Remove a localization

Deletes the localization with the given language ID if it exists

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import drafts_api
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
    api_instance = drafts_api.DraftsApi(api_client)
    draft_id = "draftId_example" # str | A draft ID
    language_id = "languageId_example" # str | A language ID (eg: en-US)
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"

    # example passing only required values which don't have defaults set
    try:
        # Remove a localization
        api_instance.delete_localization(draft_id, language_id, accept)
    except dyspatch_client.ApiException as e:
        print("Exception when calling DraftsApi->delete_localization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID |
 **language_id** | **str**| A language ID (eg: en-US) |
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful delete |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft_by_id**
> DraftRead get_draft_by_id(draft_id, target_language, accept)

Get Draft by ID

Gets a draft object with the matching ID. The \"compiled\" field will contain the template in the default, unlocalized form.

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import drafts_api
from dyspatch_client.model.draft_read import DraftRead
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
    api_instance = drafts_api.DraftsApi(api_client)
    draft_id = "draftId_example" # str | A draft ID
    target_language = "html" # str | The type of templating language to compile as. Should only be used for visual templates.
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"

    # example passing only required values which don't have defaults set
    try:
        # Get Draft by ID
        api_response = api_instance.get_draft_by_id(draft_id, target_language, accept)
        pprint(api_response)
    except dyspatch_client.ApiException as e:
        print("Exception when calling DraftsApi->get_draft_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID |
 **target_language** | **str**| The type of templating language to compile as. Should only be used for visual templates. |
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |

### Return type

[**DraftRead**](DraftRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2020.11+json, */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A draft object with the requested ID. |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**400** | Invalid request |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**401** | Unauthenticated |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**403** | Unauthorized |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**404** | Resource not found |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**429** | Rate limit exceeded |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**500** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**0** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_draft_localization_keys**
> [LocalizationKeyRead] get_draft_localization_keys(draft_id, accept)

Get localization keys

Returns the list of values that need to be translated for the draft. Set the `Accept` header to `application/vnd.dyspatch.2020.11+json` to get a JSON object, or `text/vnd.dyspatch.2020.11+x-gettext-translation` to get the POT file.

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import drafts_api
from dyspatch_client.model.localization_key_read import LocalizationKeyRead
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
    api_instance = drafts_api.DraftsApi(api_client)
    draft_id = "draftId_example" # str | A draft ID
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"

    # example passing only required values which don't have defaults set
    try:
        # Get localization keys
        api_response = api_instance.get_draft_localization_keys(draft_id, accept)
        pprint(api_response)
    except dyspatch_client.ApiException as e:
        print("Exception when calling DraftsApi->get_draft_localization_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID |
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |

### Return type

[**[LocalizationKeyRead]**](LocalizationKeyRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2020.11+json, text/vnd.dyspatch.2020.11+x-gettext-translation


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Localization keys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_drafts**
> DraftsRead get_drafts(accept)

List Drafts

Returns all drafts for your organization.

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import drafts_api
from dyspatch_client.model.drafts_read import DraftsRead
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
    api_instance = drafts_api.DraftsApi(api_client)
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"
    cursor = "cursor_example" # str | A cursor value used to retrieve a specific page from a paginated result set. (optional)
    status = "awaitingTranslation" # str | Filter the list of drafts by a particular status (optional) if omitted the server will use the default value of "awaitingTranslation"

    # example passing only required values which don't have defaults set
    try:
        # List Drafts
        api_response = api_instance.get_drafts(accept)
        pprint(api_response)
    except dyspatch_client.ApiException as e:
        print("Exception when calling DraftsApi->get_drafts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Drafts
        api_response = api_instance.get_drafts(accept, cursor=cursor, status=status)
        pprint(api_response)
    except dyspatch_client.ApiException as e:
        print("Exception when calling DraftsApi->get_drafts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |
 **cursor** | **str**| A cursor value used to retrieve a specific page from a paginated result set. | [optional]
 **status** | **str**| Filter the list of drafts by a particular status | [optional] if omitted the server will use the default value of "awaitingTranslation"

### Return type

[**DraftsRead**](DraftsRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2020.11+json, */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Drafts |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**400** | Invalid request |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**401** | Unauthenticated |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**403** | Unauthorized |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**404** | Resource not found |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**429** | Rate limit exceeded |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**500** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**0** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_localization_for_draft**
> [LocalizationMetaRead] get_localization_for_draft(draft_id, accept)

Get localizations on a draft

Returns localization metadata for the draft

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import drafts_api
from dyspatch_client.model.localization_meta_read import LocalizationMetaRead
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
    api_instance = drafts_api.DraftsApi(api_client)
    draft_id = "draftId_example" # str | A draft ID
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"

    # example passing only required values which don't have defaults set
    try:
        # Get localizations on a draft
        api_response = api_instance.get_localization_for_draft(draft_id, accept)
        pprint(api_response)
    except dyspatch_client.ApiException as e:
        print("Exception when calling DraftsApi->get_localization_for_draft: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID |
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |

### Return type

[**[LocalizationMetaRead]**](LocalizationMetaRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2020.11+json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of localizations |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_localization**
> save_localization(draft_id, language_id, accept, inline_object)

Create or update a localization

Inserts a localization or sets the name on an existing localization that already uses the languageId

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import drafts_api
from dyspatch_client.model.inline_object import InlineObject
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
    api_instance = drafts_api.DraftsApi(api_client)
    draft_id = "draftId_example" # str | A draft ID
    language_id = "languageId_example" # str | A language ID (eg: en-US)
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"
    inline_object = InlineObject(
        name="English (US)",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Create or update a localization
        api_instance.save_localization(draft_id, language_id, accept, inline_object)
    except dyspatch_client.ApiException as e:
        print("Exception when calling DraftsApi->save_localization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID |
 **language_id** | **str**| A language ID (eg: en-US) |
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful upsert |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_translation**
> set_translation(draft_id, language_id, accept, request_body)

Set translations for language

Completely replaces any existing translations for the given language with those provided in request body. Variables embedded in keys or values are expected to be in the format `%(my_variable)s` and will automatically convert to the correct Dyspatch format depending on the type of template. Accepts key/value pairs in JSON format or in gettext PO file format. For JSON set `Content-Type` header to `application/json`. For gettext PO format set `Content-Type` header to `text/x-gettext-translation`.

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import drafts_api
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
    api_instance = drafts_api.DraftsApi(api_client)
    draft_id = "draftId_example" # str | A draft ID
    language_id = "languageId_example" # str | A language ID (eg: en-US)
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"
    request_body = {
        "key": "key_example",
    } # {str: (str,)} | 

    # example passing only required values which don't have defaults set
    try:
        # Set translations for language
        api_instance.set_translation(draft_id, language_id, accept, request_body)
    except dyspatch_client.ApiException as e:
        print("Exception when calling DraftsApi->set_translation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID |
 **language_id** | **str**| A language ID (eg: en-US) |
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |
 **request_body** | **{str: (str,)}**|  |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |
**403** | Unauthorized |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_draft_for_approval**
> submit_draft_for_approval(draft_id, accept)

Submit the draft for approval

Moves the draft into submitted state.

### Example

* Api Key Authentication (Bearer):
```python
import time
import dyspatch_client
from dyspatch_client.api import drafts_api
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
    api_instance = drafts_api.DraftsApi(api_client)
    draft_id = "draftId_example" # str | A draft ID
    accept = "Accept_example" # str | A version of the API that should be used for the request. For example, to use version \"2020.11\", set the value to \"application/vnd.dyspatch.2020.11+json\"

    # example passing only required values which don't have defaults set
    try:
        # Submit the draft for approval
        api_instance.submit_draft_for_approval(draft_id, accept)
    except dyspatch_client.ApiException as e:
        print("Exception when calling DraftsApi->submit_draft_for_approval: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID |
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2020.11\&quot;, set the value to \&quot;application/vnd.dyspatch.2020.11+json\&quot; |

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully submitted |  -  |
**400** | Invalid request |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**401** | Unauthenticated |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**403** | Unauthorized |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**404** | Resource not found |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**429** | Rate limit exceeded |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**500** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |
**0** | Server error |  * X-RateLimit-Remaining - The number of requests left for the current time window <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

