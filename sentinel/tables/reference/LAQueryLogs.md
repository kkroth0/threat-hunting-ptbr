# LAQueryLogs

## Objetivo de caça
Log Analytics consulta dados de auditoria para revisão de consultas, consultas caras e governança de atividades de caça.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `StatsDataProcessedEnd` | `datetime` |
| `StatsDataProcessedStart` | `datetime` |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
LAQueryLogs
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
LAQueryLogs
| where TimeGenerated >= ago(24h)
| project StatsDataProcessedEnd, StatsDataProcessedStart, TimeGenerated, _ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AADClientId` | `string` |
| `AADEmail` | `string` |
| `AADObjectId` | `string` |
| `AADTenantId` | `string` |
| `ConditionalDataAccess` | `string` |
| `CorrelationId` | `string` |
| `IsBillableQuery` | `bool` |
| `IsWorkspaceInFailover` | `bool` |
| `QueryText` | `string` |
| `QueryThumbprint` | `string` |
| `QueryTimeRangeEnd` | `datetime` |
| `QueryTimeRangeStart` | `datetime` |
| `RecordKind` | `string` |
| `RequestClientApp` | `string` |
| `RequestContext` | `dynamic` |
| `RequestContextFilters` | `dynamic` |
| `RequestTarget` | `string` |
| `ResponseCode` | `int` |
| `ResponseDurationMs` | `real` |
| `ResponseRowCount` | `int` |
| `ScannedGB` | `real` |
| `SourceSystem` | `string` |
| `StatsCPUTimeMs` | `real` |
| `StatsDataProcessedEnd` | `datetime` |
| `StatsDataProcessedStart` | `datetime` |
| `StatsRegionCount` | `int` |
| `StatsWorkspaceCount` | `int` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `WorkspaceRegion` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
