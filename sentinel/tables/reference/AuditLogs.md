# AuditLogs

## Objetivo de caça
atividade de auditoria Microsoft Entra ID para alterações de diretório, função, aplicativo, política e administrativas.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `AADOperationType` | `string` |
| `ActivityDateTime` | `datetime` |
| `ActivityDisplayName` | `string` |
| `Identity` | `string` |
| `Location` | `string` |
| `OperationName` | `string` |
| `OperationVersion` | `string` |
| `Resource` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceProvider` | `string` |
| `TargetResources` | `dynamic` |
| `TimeGenerated` | `datetime` |

## Consulta inicial
```kql
AuditLogs
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
AuditLogs
| where TimeGenerated >= ago(24h)
| project AADOperationType, ActivityDateTime, ActivityDisplayName, Identity, Location, OperationName, OperationVersion, Resource
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AADOperationType` | `string` |
| `AADTenantId` | `string` |
| `ActivityDateTime` | `datetime` |
| `ActivityDisplayName` | `string` |
| `AdditionalDetails` | `dynamic` |
| `Category` | `string` |
| `CorrelationId` | `string` |
| `DurationMs` | `long` |
| `Id` | `string` |
| `Identity` | `string` |
| `InitiatedBy` | `dynamic` |
| `Level` | `string` |
| `Location` | `string` |
| `LoggedByService` | `string` |
| `OperationName` | `string` |
| `OperationVersion` | `string` |
| `Resource` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceProvider` | `string` |
| `Result` | `string` |
| `ResultDescription` | `string` |
| `ResultReason` | `string` |
| `ResultSignature` | `string` |
| `ResultType` | `string` |
| `SourceSystem` | `string` |
| `TargetResources` | `dynamic` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
