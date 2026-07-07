# TrendMicro_XDR_OAT_Health_Check_CL

## Objetivo de caça
Tabela customizada Trend Vision One usada para integridade, detecção ou busca no ambiente de trabalho endpoint/XDR.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `Computer` | `string` |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
TrendMicro_XDR_OAT_Health_Check_CL
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
TrendMicro_XDR_OAT_Health_Check_CL
| where TimeGenerated >= ago(24h)
| project Computer, TimeGenerated, _ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `clpId_g` | `string` |
| `Computer` | `string` |
| `error_s` | `string` |
| `queryEndTime_t` | `datetime` |
| `queryStartTime_t` | `datetime` |
| `RawData` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
