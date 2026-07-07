# SentinelHealth

## Objetivo de caça
Registros de integridade Sentinel para conectores, análises, automação e monitoramento operacional.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `OperationName` | `string` |
| `SentinelResourceId` | `string` |
| `SentinelResourceKind` | `string` |
| `SentinelResourceName` | `string` |
| `SentinelResourceType` | `string` |
| `Status` | `string` |
| `TimeGenerated` | `datetime` |

## Consulta inicial
```kql
SentinelHealth
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
SentinelHealth
| where TimeGenerated >= ago(24h)
| project OperationName, SentinelResourceId, SentinelResourceKind, SentinelResourceName, SentinelResourceType, Status, TimeGenerated
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `Description` | `string` |
| `ExtendedProperties` | `dynamic` |
| `OperationName` | `string` |
| `Reason` | `string` |
| `RecordId` | `string` |
| `SentinelResourceId` | `string` |
| `SentinelResourceKind` | `string` |
| `SentinelResourceName` | `string` |
| `SentinelResourceType` | `string` |
| `SourceSystem` | `string` |
| `Status` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `WorkspaceId` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
