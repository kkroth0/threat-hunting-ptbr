# AMAAgentHealth_CL

## Objetivo de caça
Tabela Sentinel/Log Analytics disponível para busca e correlação.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
AMAAgentHealth_CL
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
AMAAgentHealth_CL
| where TimeGenerated >= ago(24h)
| project TimeGenerated, _ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `RawData` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
