# FunctionAppLogs

## Objetivo de caça
Tabela Sentinel/Log Analytics disponível para busca e correlação.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `ActivityId` | `string` |
| `EventId` | `int` |
| `HostInstanceId` | `string` |
| `HostVersion` | `string` |
| `Location` | `string` |
| `ProcessId` | `int` |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
FunctionAppLogs
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
FunctionAppLogs
| where TimeGenerated >= ago(24h)
| project ActivityId, EventId, HostInstanceId, HostVersion, Location, ProcessId, TimeGenerated, _ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `ActivityId` | `string` |
| `AppName` | `string` |
| `Category` | `string` |
| `EventId` | `int` |
| `EventName` | `string` |
| `ExceptionDetails` | `string` |
| `ExceptionMessage` | `string` |
| `ExceptionType` | `string` |
| `FunctionInvocationId` | `string` |
| `FunctionName` | `string` |
| `HostInstanceId` | `string` |
| `HostVersion` | `string` |
| `Level` | `string` |
| `LevelId` | `int` |
| `Location` | `string` |
| `Message` | `string` |
| `ProcessId` | `int` |
| `RoleInstance` | `string` |
| `SourceSystem` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
