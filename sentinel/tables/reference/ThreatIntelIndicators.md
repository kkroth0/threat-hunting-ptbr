# ThreatIntelIndicators

## Objetivo de caça
Indicadores de inteligência de ameaças armazenados em Sentinel para correspondência IOC e buscas orientadas por inteligência.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
ThreatIntelIndicators
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
ThreatIntelIndicators
| where TimeGenerated >= ago(24h)
| project TimeGenerated, _ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AdditionalFields` | `dynamic` |
| `AzureTenantId` | `string` |
| `Confidence` | `int` |
| `Created` | `datetime` |
| `Data` | `dynamic` |
| `Id` | `string` |
| `IsActive` | `bool` |
| `IsDeleted` | `bool` |
| `LastUpdateMethod` | `string` |
| `Modified` | `datetime` |
| `ObservableKey` | `string` |
| `ObservableValue` | `string` |
| `Pattern` | `string` |
| `Revoked` | `bool` |
| `SourceSystem` | `string` |
| `Tags` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `ValidFrom` | `datetime` |
| `ValidUntil` | `datetime` |
| `WorkspaceId` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
