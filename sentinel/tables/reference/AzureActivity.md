# AzureActivity

## Objetivo de caça
Azure operações de plano de controle para alterações de recursos, falhas, atribuições de funções e atividades de assinatura.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `ActivityStatus` | `string` |
| `ActivityStatusValue` | `string` |
| `ActivitySubstatus` | `string` |
| `ActivitySubstatusValue` | `string` |
| `CallerIpAddress` | `string` |
| `OperationId` | `string` |
| `OperationName` | `string` |
| `OperationNameValue` | `string` |
| `Resource` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceProvider` | `string` |
| `ResourceProviderValue` | `string` |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
AzureActivity
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
AzureActivity
| where TimeGenerated >= ago(24h)
| project ActivityStatus, ActivityStatusValue, ActivitySubstatus, ActivitySubstatusValue, CallerIpAddress, OperationId, OperationName, OperationNameValue
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `ActivityStatus` | `string` |
| `ActivityStatusValue` | `string` |
| `ActivitySubstatus` | `string` |
| `ActivitySubstatusValue` | `string` |
| `Authorization` | `string` |
| `Authorization_d` | `dynamic` |
| `Caller` | `string` |
| `CallerIpAddress` | `string` |
| `Category` | `string` |
| `CategoryValue` | `string` |
| `Claims` | `string` |
| `Claims_d` | `dynamic` |
| `CorrelationId` | `string` |
| `EventDataId` | `string` |
| `EventSubmissionTimestamp` | `datetime` |
| `Hierarchy` | `string` |
| `HTTPRequest` | `string` |
| `Level` | `string` |
| `OperationId` | `string` |
| `OperationName` | `string` |
| `OperationNameValue` | `string` |
| `Properties` | `string` |
| `Properties_d` | `dynamic` |
| `Resource` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceProvider` | `string` |
| `ResourceProviderValue` | `string` |
| `SourceSystem` | `string` |
| `SubscriptionId` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
