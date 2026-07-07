# Anomalies

## Objetivo de caça
registros de anomalias Sentinel para análise de comportamento e detecção.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `ActivityInsights` | `dynamic` |
| `DestinationDevice` | `string` |
| `DestinationIpAddress` | `string` |
| `DestinationLocation` | `dynamic` |
| `DeviceInsights` | `dynamic` |
| `RuleStatus` | `string` |
| `SourceDevice` | `string` |
| `SourceIpAddress` | `string` |
| `SourceLocation` | `dynamic` |
| `Tactics` | `string` |
| `Techniques` | `string` |
| `TimeGenerated` | `datetime` |
| `UserInsights` | `dynamic` |
| `UserName` | `string` |
| `UserPrincipalName` | `string` |

## Consulta inicial
```kql
Anomalies
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
Anomalies
| where TimeGenerated >= ago(24h)
| project ActivityInsights, DestinationDevice, DestinationIpAddress, DestinationLocation, DeviceInsights, RuleStatus, SourceDevice, SourceIpAddress
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `ActivityInsights` | `dynamic` |
| `AnomalyDetails` | `dynamic` |
| `AnomalyReasons` | `dynamic` |
| `AnomalyTemplateId` | `string` |
| `AnomalyTemplateName` | `string` |
| `AnomalyTemplateVersion` | `string` |
| `Description` | `string` |
| `DestinationDevice` | `string` |
| `DestinationIpAddress` | `string` |
| `DestinationLocation` | `dynamic` |
| `DeviceInsights` | `dynamic` |
| `EndTime` | `datetime` |
| `Entities` | `dynamic` |
| `ExtendedLinks` | `dynamic` |
| `ExtendedProperties` | `dynamic` |
| `Id` | `string` |
| `RuleConfigVersion` | `string` |
| `RuleId` | `string` |
| `RuleName` | `string` |
| `RuleStatus` | `string` |
| `Score` | `real` |
| `SourceDevice` | `string` |
| `SourceIpAddress` | `string` |
| `SourceLocation` | `dynamic` |
| `SourceSystem` | `string` |
| `StartTime` | `datetime` |
| `Tactics` | `string` |
| `Techniques` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `UserInsights` | `dynamic` |
| `UserName` | `string` |
| `UserPrincipalName` | `string` |
| `VendorName` | `string` |
| `WorkspaceId` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
