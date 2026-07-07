# SecurityAlert

## Objetivo de caça
Registros de alerta produzidos pela Microsoft e produtos de segurança conectados.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `AlertLink` | `string` |
| `AlertName` | `string` |
| `AlertSeverity` | `string` |
| `AlertType` | `string` |
| `IsIncident` | `bool` |
| `ProcessingEndTime` | `datetime` |
| `ResourceId` | `string` |
| `SourceComputerId` | `string` |
| `Status` | `string` |
| `SubTechniques` | `string` |
| `SystemAlertId` | `string` |
| `Tactics` | `string` |
| `Techniques` | `string` |
| `TimeGenerated` | `datetime` |
| `WorkspaceResourceGroup` | `string` |

## Consulta inicial
```kql
SecurityAlert
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
SecurityAlert
| where TimeGenerated >= ago(24h)
| project AlertLink, AlertName, AlertSeverity, AlertType, IsIncident, ProcessingEndTime, ResourceId, SourceComputerId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AlertLink` | `string` |
| `AlertName` | `string` |
| `AlertSeverity` | `string` |
| `AlertType` | `string` |
| `CompromisedEntity` | `string` |
| `ConfidenceLevel` | `string` |
| `ConfidenceScore` | `real` |
| `Description` | `string` |
| `DisplayName` | `string` |
| `EndTime` | `datetime` |
| `Entities` | `string` |
| `ExtendedLinks` | `string` |
| `ExtendedProperties` | `string` |
| `IsIncident` | `bool` |
| `ProcessingEndTime` | `datetime` |
| `ProductComponentName` | `string` |
| `ProductName` | `string` |
| `ProviderName` | `string` |
| `RemediationSteps` | `string` |
| `ResourceId` | `string` |
| `SourceComputerId` | `string` |
| `StartTime` | `datetime` |
| `Status` | `string` |
| `SubTechniques` | `string` |
| `SystemAlertId` | `string` |
| `Tactics` | `string` |
| `Techniques` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `VendorName` | `string` |
| `VendorOriginalId` | `string` |
| `WorkspaceResourceGroup` | `string` |
| `WorkspaceSubscriptionId` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
