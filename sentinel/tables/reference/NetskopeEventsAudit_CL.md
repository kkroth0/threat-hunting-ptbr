# NetskopeEventsAudit_CL

## Objetivo de caça
Tabela personalizada Netskope usada para SASE, CASB, web, DLP, aplicativo e busca de rede.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `sAMAccountName` | `string` |
| `severity_level` | `int` |
| `TimeGenerated` | `datetime` |
| `user` | `string` |
| `userPrincipalName` | `string` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
NetskopeEventsAudit_CL
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
NetskopeEventsAudit_CL
| where TimeGenerated >= ago(24h)
| project sAMAccountName, severity_level, TimeGenerated, user, userPrincipalName, _ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `audit_log_event` | `string` |
| `ccl` | `string` |
| `count_i` | `int` |
| `organization_unit` | `string` |
| `sAMAccountName` | `string` |
| `severity_level` | `int` |
| `supporting_data` | `dynamic` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `timestamp` | `int` |
| `Type` | `string` |
| `type_s` | `string` |
| `ur_normalized` | `string` |
| `user` | `string` |
| `userPrincipalName` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
