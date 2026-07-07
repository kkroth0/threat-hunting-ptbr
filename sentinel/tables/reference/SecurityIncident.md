# SecurityIncident

## Objetivo de caça
registros de incidentes Microsoft Sentinel para gerenciamento de casos, qualidade de triagem e revisão do ciclo de vida de incidentes.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `AlertIds` | `dynamic` |
| `FirstActivityTime` | `datetime` |
| `IncidentName` | `string` |
| `IncidentNumber` | `int` |
| `IncidentUrl` | `string` |
| `LastActivityTime` | `datetime` |
| `ProviderIncidentId` | `string` |
| `Severity` | `string` |
| `Status` | `string` |
| `TimeGenerated` | `datetime` |

## Consulta inicial
```kql
SecurityIncident
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
SecurityIncident
| where TimeGenerated >= ago(24h)
| project AlertIds, FirstActivityTime, IncidentName, IncidentNumber, IncidentUrl, LastActivityTime, ProviderIncidentId, Severity
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AdditionalData` | `dynamic` |
| `AlertIds` | `dynamic` |
| `BookmarkIds` | `dynamic` |
| `Classification` | `string` |
| `ClassificationComment` | `string` |
| `ClassificationReason` | `string` |
| `ClosedTime` | `datetime` |
| `Comments` | `dynamic` |
| `CreatedTime` | `datetime` |
| `Description` | `string` |
| `FirstActivityTime` | `datetime` |
| `FirstModifiedTime` | `datetime` |
| `IncidentName` | `string` |
| `IncidentNumber` | `int` |
| `IncidentUrl` | `string` |
| `Labels` | `dynamic` |
| `LastActivityTime` | `datetime` |
| `LastModifiedTime` | `datetime` |
| `ModifiedBy` | `string` |
| `Owner` | `dynamic` |
| `ProviderIncidentId` | `string` |
| `ProviderName` | `string` |
| `RelatedAnalyticRuleIds` | `dynamic` |
| `Severity` | `string` |
| `SourceSystem` | `string` |
| `Status` | `string` |
| `Tasks` | `dynamic` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Title` | `string` |
| `Type` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
