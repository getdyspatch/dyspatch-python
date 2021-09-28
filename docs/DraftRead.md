# DraftRead

template draft metadata included latest draft revision

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An opaque, unique identifier for a draft | [optional] 
**template** | **str** | An opaque, unique identifier for a template | [optional] 
**name** | **str** | The name of a draft | [optional] 
**url** | **str** | The API url for a specific draft | [optional] 
**compiled** | [**CompiledRead**](CompiledRead.md) |  | [optional] 
**created_at** | **datetime** | The time of initial creation | [optional] 
**updated_at** | **datetime** | The time of last update | [optional] 
**localizations** | [**[LocalizationMetaRead]**](LocalizationMetaRead.md) | A list of the Template&#39;s available localizations | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


