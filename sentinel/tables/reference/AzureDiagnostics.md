# AzureDiagnostics

## Objetivo de caça
Azure diagnósticos de recursos e logs de serviço para busca em nível de plataforma e recurso.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `actionCount_d` | `real` |
| `Computer` | `string` |
| `correlation_actionTrackingId_g` | `string` |
| `location_s` | `string` |
| `OperationName` | `string` |
| `Resource` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceProvider` | `string` |
| `ResourceType` | `string` |
| `resource_actionName_s` | `string` |
| `resource_location_s` | `string` |
| `resource_originRunId_s` | `string` |
| `resource_resourceGroupName_s` | `string` |
| `resource_runId_s` | `string` |
| `resource_sourceTriggerHistoryName_s` | `string` |
| `resource_subscriptionId_g` | `string` |
| `resource_triggerName_s` | `string` |
| `resource_workflowId_g` | `string` |
| `resource_workflowName_s` | `string` |
| `status_s` | `string` |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
AzureDiagnostics
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
AzureDiagnostics
| where TimeGenerated >= ago(24h)
| project actionCount_d, Computer, correlation_actionTrackingId_g, location_s, OperationName, Resource, ResourceGroup, ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `actionCount_d` | `real` |
| `AdditionalFields` | `dynamic` |
| `Category` | `string` |
| `code_s` | `string` |
| `Computer` | `string` |
| `CorrelationId` | `string` |
| `correlation_actionTrackingId_g` | `string` |
| `correlation_clientKeywords_s` | `string` |
| `correlation_clientTrackingId_g` | `string` |
| `correlation_clientTrackingId_s` | `string` |
| `endTime_t` | `datetime` |
| `error_code_s` | `string` |
| `error_message_s` | `string` |
| `executionClusterType_s` | `string` |
| `fired_b` | `bool` |
| `isV2Threshold_b` | `bool` |
| `Level` | `string` |
| `location_s` | `string` |
| `metadataOverflowContentLength_d` | `real` |
| `OperationName` | `string` |
| `RawData` | `string` |
| `Resource` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceProvider` | `string` |
| `ResourceType` | `string` |
| `resource_actionName_s` | `string` |
| `resource_location_s` | `string` |
| `resource_originRunId_s` | `string` |
| `resource_resourceGroupName_s` | `string` |
| `resource_runId_s` | `string` |
| `resource_sourceTriggerHistoryName_s` | `string` |
| `resource_subscriptionId_g` | `string` |
| `resource_triggerName_s` | `string` |
| `resource_workflowId_g` | `string` |
| `resource_workflowName_s` | `string` |
| `ResultDescription` | `string` |
| `ResultType` | `string` |
| `retryHistory_s` | `string` |
| `SourceSystem` | `string` |
| `startTime_t` | `datetime` |
| `status_s` | `string` |
| `SubscriptionId` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `workflowId_s` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_schema_s` | `string` |
| `_SubscriptionId` | `string` |
