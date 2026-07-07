# AppDependencies

## Objetivo de caça
Telemetria do Application Insights para comportamento de aplicativos, dependências, exceções, solicitações, rastreamentos, métricas e busca de desempenho.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `ClientIP` | `string` |
| `OperationId` | `string` |
| `OperationName` | `string` |
| `ResourceGUID` | `string` |
| `TimeGenerated` | `datetime` |
| `UserAccountId` | `string` |
| `UserAuthenticatedId` | `string` |
| `UserId` | `string` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
AppDependencies
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
AppDependencies
| where TimeGenerated >= ago(24h)
| project ClientIP, OperationId, OperationName, ResourceGUID, TimeGenerated, UserAccountId, UserAuthenticatedId, UserId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AppRoleInstance` | `string` |
| `AppRoleName` | `string` |
| `AppVersion` | `string` |
| `ClientBrowser` | `string` |
| `ClientCity` | `string` |
| `ClientCountryOrRegion` | `string` |
| `ClientIP` | `string` |
| `ClientModel` | `string` |
| `ClientOS` | `string` |
| `ClientStateOrProvince` | `string` |
| `ClientType` | `string` |
| `Data` | `string` |
| `DependencyType` | `string` |
| `DurationMs` | `real` |
| `Id` | `string` |
| `IKey` | `string` |
| `ItemCount` | `int` |
| `Measurements` | `dynamic` |
| `Name` | `string` |
| `OperationId` | `string` |
| `OperationName` | `string` |
| `ParentId` | `string` |
| `Properties` | `dynamic` |
| `ReferencedItemId` | `string` |
| `ReferencedType` | `string` |
| `ResourceGUID` | `string` |
| `ResultCode` | `string` |
| `SDKVersion` | `string` |
| `SessionId` | `string` |
| `SourceSystem` | `string` |
| `Success` | `bool` |
| `SyntheticSource` | `string` |
| `Target` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `UserAccountId` | `string` |
| `UserAuthenticatedId` | `string` |
| `UserId` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
