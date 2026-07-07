# BehaviorAnalytics

## Objetivo de caça
Saída de comportamento UEBA usada para risco de entidade, anomalia e investigação baseada em pares.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `ActionType` | `string` |
| `ActivityInsights` | `dynamic` |
| `ActivityType` | `string` |
| `DestinationDevice` | `string` |
| `DestinationIPAddress` | `string` |
| `DestinationIPLocation` | `string` |
| `Device` | `string` |
| `DevicesInsights` | `dynamic` |
| `SourceDevice` | `string` |
| `SourceIPAddress` | `string` |
| `SourceIPLocation` | `string` |
| `TimeGenerated` | `datetime` |
| `TimeProcessed` | `datetime` |
| `UserName` | `string` |
| `UserPrincipalName` | `string` |
| `UsersInsights` | `dynamic` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
BehaviorAnalytics
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
BehaviorAnalytics
| where TimeGenerated >= ago(24h)
| project ActionType, ActivityInsights, ActivityType, DestinationDevice, DestinationIPAddress, DestinationIPLocation, Device, DevicesInsights
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `ActionType` | `string` |
| `ActivityInsights` | `dynamic` |
| `ActivityType` | `string` |
| `ActorName` | `string` |
| `ActorPrincipalName` | `string` |
| `DestinationDevice` | `string` |
| `DestinationIPAddress` | `string` |
| `DestinationIPLocation` | `string` |
| `Device` | `string` |
| `DevicesInsights` | `dynamic` |
| `EventProductVersion` | `string` |
| `EventSource` | `string` |
| `EventVendor` | `string` |
| `InvestigationPriority` | `int` |
| `NativeTableName` | `string` |
| `SourceDevice` | `string` |
| `SourceIPAddress` | `string` |
| `SourceIPLocation` | `string` |
| `SourceRecordId` | `string` |
| `SourceSystem` | `string` |
| `TargetName` | `string` |
| `TargetPrincipalName` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `TimeProcessed` | `datetime` |
| `Type` | `string` |
| `UserName` | `string` |
| `UserPrincipalName` | `string` |
| `UsersInsights` | `dynamic` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
