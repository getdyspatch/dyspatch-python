# dyspatch_client.DraftsApi

All URIs are relative to *https://api.dyspatch.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**drafts_draft_id_get**](DraftsApi.md#drafts_draft_id_get) | **GET** /drafts/{draftId} | Get Draft by ID
[**drafts_draft_id_localization_keys_get**](DraftsApi.md#drafts_draft_id_localization_keys_get) | **GET** /drafts/{draftId}/localizationKeys | Get Localization Keys
[**drafts_draft_id_localizations_get**](DraftsApi.md#drafts_draft_id_localizations_get) | **GET** /drafts/{draftId}/localizations | Get Localizations on a Draft
[**drafts_draft_id_localizations_language_id_delete**](DraftsApi.md#drafts_draft_id_localizations_language_id_delete) | **DELETE** /drafts/{draftId}/localizations/{languageId} | Remove a Localization
[**drafts_draft_id_localizations_language_id_put**](DraftsApi.md#drafts_draft_id_localizations_language_id_put) | **PUT** /drafts/{draftId}/localizations/{languageId} | Create or Update a Localization
[**drafts_draft_id_localizations_language_id_translations_put**](DraftsApi.md#drafts_draft_id_localizations_language_id_translations_put) | **PUT** /drafts/{draftId}/localizations/{languageId}/translations | Set Translations for Language
[**drafts_draft_id_publish_request_post**](DraftsApi.md#drafts_draft_id_publish_request_post) | **POST** /drafts/{draftId}/publishRequest | Submit the Draft for Approval
[**drafts_get**](DraftsApi.md#drafts_get) | **GET** /drafts | List Drafts


# **drafts_draft_id_get**
> DraftRead drafts_draft_id_get(draft_id, target_language)

Get Draft by ID

Gets a draft object with the matching ID. The \"compiled\" field will contain the unlocalized default template object.

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
api_instance = dyspatch_client.DraftsApi(dyspatch_client.ApiClient(configuration))
draft_id = 'draft_id_example' # str | A draft ID
target_language = 'target_language_example' # str | The type of templating language to compile as. Should only be used for visual templates.

try:
    # Get Draft by ID
    api_response = api_instance.drafts_draft_id_get(draft_id, target_language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftsApi->drafts_draft_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID | 
 **target_language** | **str**| The type of templating language to compile as. Should only be used for visual templates. | 

### Return type

[**DraftRead**](DraftRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2019.10+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drafts_draft_id_localization_keys_get**
> list[LocalizationKeyRead] drafts_draft_id_localization_keys_get(draft_id, accept=accept)

Get Localization Keys

Returns the list of values that need to be translated for the draft. Set the `Accept` header to `application/vnd.dyspatch.2019.10+json` to get a JSON object, or `text/vnd.dyspatch.2019.10+x-gettext-translation` to get the POT file.

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
api_instance = dyspatch_client.DraftsApi(dyspatch_client.ApiClient(configuration))
draft_id = 'draft_id_example' # str | A draft ID
accept = 'accept_example' # str | A version of the API that should be used for the request. For example, to use version \"2019.10\", set the value to \"application/vnd.dyspatch.2019.10+json\". (optional)

try:
    # Get Localization Keys
    api_response = api_instance.drafts_draft_id_localization_keys_get(draft_id, accept=accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftsApi->drafts_draft_id_localization_keys_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID | 
 **accept** | **str**| A version of the API that should be used for the request. For example, to use version \&quot;2019.10\&quot;, set the value to \&quot;application/vnd.dyspatch.2019.10+json\&quot;. | [optional] 

### Return type

[**list[LocalizationKeyRead]**](LocalizationKeyRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2019.10+json, text/vnd.dyspatch.2019.10+x-gettext-translation

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drafts_draft_id_localizations_get**
> list[LocalizationMetaRead] drafts_draft_id_localizations_get(draft_id)

Get Localizations on a Draft

Returns localization metadata object for a template draft.

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
api_instance = dyspatch_client.DraftsApi(dyspatch_client.ApiClient(configuration))
draft_id = 'draft_id_example' # str | A draft ID

try:
    # Get Localizations on a Draft
    api_response = api_instance.drafts_draft_id_localizations_get(draft_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftsApi->drafts_draft_id_localizations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID | 

### Return type

[**list[LocalizationMetaRead]**](LocalizationMetaRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2019.10+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drafts_draft_id_localizations_language_id_delete**
> drafts_draft_id_localizations_language_id_delete(draft_id, language_id)

Remove a Localization

Deletes the localization with the given `languageId` if it exists.

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
api_instance = dyspatch_client.DraftsApi(dyspatch_client.ApiClient(configuration))
draft_id = 'draft_id_example' # str | A draft ID
language_id = 'language_id_example' # str | A language ID (eg: en-US)

try:
    # Remove a Localization
    api_instance.drafts_draft_id_localizations_language_id_delete(draft_id, language_id)
except ApiException as e:
    print("Exception when calling DraftsApi->drafts_draft_id_localizations_language_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID | 
 **language_id** | **str**| A language ID (eg: en-US) | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2019.10+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drafts_draft_id_localizations_language_id_put**
> drafts_draft_id_localizations_language_id_put(draft_id, language_id, body)

Create or Update a Localization

Inserts a localization or sets the name on an existing localization that already uses the `languageId`.

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
api_instance = dyspatch_client.DraftsApi(dyspatch_client.ApiClient(configuration))
draft_id = 'draft_id_example' # str | A draft ID
language_id = 'language_id_example' # str | A language ID (eg: en-US)
body = dyspatch_client.Body() # Body | 

try:
    # Create or Update a Localization
    api_instance.drafts_draft_id_localizations_language_id_put(draft_id, language_id, body)
except ApiException as e:
    print("Exception when calling DraftsApi->drafts_draft_id_localizations_language_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID | 
 **language_id** | **str**| A language ID (eg: en-US) | 
 **body** | [**Body**](Body.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2019.10+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drafts_draft_id_localizations_language_id_translations_put**
> drafts_draft_id_localizations_language_id_translations_put(draft_id, language_id, body)

Set Translations for Language

Completely replaces any existing translations for the given language with those provided in request body. Variables embedded in keys or values are expected to be in the format `%(my_variable)s` and will automatically convert to the correct Dyspatch format depending on the type of template. Accepts key/value pairs in JSON format or in gettext PO file format. For JSON set `Content-Type` header to `application/json`. For gettext PO format set `Content-Type` header to `text/x-gettext-translation`.

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
api_instance = dyspatch_client.DraftsApi(dyspatch_client.ApiClient(configuration))
draft_id = 'draft_id_example' # str | A draft ID
language_id = 'language_id_example' # str | A language ID (eg: en-US)
body = NULL # object | 

try:
    # Set Translations for Language
    api_instance.drafts_draft_id_localizations_language_id_translations_put(draft_id, language_id, body)
except ApiException as e:
    print("Exception when calling DraftsApi->drafts_draft_id_localizations_language_id_translations_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID | 
 **language_id** | **str**| A language ID (eg: en-US) | 
 **body** | **object**|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2019.10+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drafts_draft_id_publish_request_post**
> drafts_draft_id_publish_request_post(draft_id)

Submit the Draft for Approval

Moves the draft into [submitted and locked state](https://docs.dyspatch.io/templates/submitting_a_template/#awaiting-approval). This will allow your email stakeholders to review the template draft and provide feedback.

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
api_instance = dyspatch_client.DraftsApi(dyspatch_client.ApiClient(configuration))
draft_id = 'draft_id_example' # str | A draft ID

try:
    # Submit the Draft for Approval
    api_instance.drafts_draft_id_publish_request_post(draft_id)
except ApiException as e:
    print("Exception when calling DraftsApi->drafts_draft_id_publish_request_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **draft_id** | **str**| A draft ID | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2019.10+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **drafts_get**
> DraftsRead drafts_get(status=status)

List Drafts

Gets a list of all drafts for your oranization. Up to 25 results returned before results are paginated.

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
api_instance = dyspatch_client.DraftsApi(dyspatch_client.ApiClient(configuration))
status = 'status_example' # str | Filter the list of drafts by a particular status (optional)

try:
    # List Drafts
    api_response = api_instance.drafts_get(status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DraftsApi->drafts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Filter the list of drafts by a particular status | [optional] 

### Return type

[**DraftsRead**](DraftsRead.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.dyspatch.2019.10+json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

