# AppSystemEvents

## Objetivo de caça
Telemetria do Application Insights para comportamento de aplicativos, dependências, exceções, solicitações, rastreamentos, métricas e busca de desempenho.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
AppSystemEvents
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
AppSystemEvents
| where TimeGenerated >= ago(24h)
| project TimeGenerated, _ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `EventType` | `string` |
| `Measurements` | `dynamic` |
| `Name` | `string` |
| `Properties` | `dynamic` |
| `SourceSystem` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
