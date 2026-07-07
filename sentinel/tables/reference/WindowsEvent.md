# WindowsEvent

## Objetivo de caça
Windows Logs de eventos coletados com AMA, úteis para endpoint específico do provedor e buscas PowerShell.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `Computer` | `string` |
| `EventID` | `int` |
| `SystemProcessId` | `int` |
| `SystemUserId` | `string` |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
WindowsEvent
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
WindowsEvent
| where TimeGenerated >= ago(24h)
| project Computer, EventID, SystemProcessId, SystemUserId, TimeGenerated, _ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `Channel` | `string` |
| `Computer` | `string` |
| `Correlation` | `string` |
| `EventData` | `dynamic` |
| `EventID` | `int` |
| `EventLevel` | `int` |
| `EventLevelName` | `string` |
| `EventOriginId` | `string` |
| `EventRecordId` | `string` |
| `Keywords` | `string` |
| `ManagementGroupName` | `string` |
| `Opcode` | `string` |
| `Provider` | `string` |
| `RawEventData` | `string` |
| `SystemProcessId` | `int` |
| `SystemThreadId` | `int` |
| `SystemUserId` | `string` |
| `Task` | `int` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `Version` | `int` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
