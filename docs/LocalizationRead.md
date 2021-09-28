# LocalizationRead

localization metadata and latest revision for associated template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An opaque, unique identifier for a localization | [optional] 
**languages** | [**Languages**](Languages.md) |  | [optional] 
**url** | **str** | The API url for a specific localization | [optional] 
**template** | **str** | An opaque, unique identifier for a template | [optional] 
**compiled** | [**CompiledRead**](CompiledRead.md) |  | [optional] 
**created_at** | **datetime** | The time of initial creation | [optional] 
**updated_at** | **datetime** | The time of last update | [optional] 
**name** | **str** | The user-specified name of a localization | [optional] 
**locale_group** | **str** | the locale group this localization belongs to, if this field is empty the localization does not belong to any locale group | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


