# IdentityInfo

## Objetivo de caça
enriquecimento de identidade UEBA que ajuda a unir detalhes da conta, tags, funções e contexto de identidade para buscar resultados.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `AccountCloudSID` | `string` |
| `AccountCreationTime` | `datetime` |
| `AccountDisplayName` | `string` |
| `AccountDomain` | `string` |
| `AccountName` | `string` |
| `AccountObjectId` | `string` |
| `AccountSID` | `string` |
| `AccountTenantId` | `string` |
| `AccountUPN` | `string` |
| `EntityRiskScore` | `dynamic` |
| `IsAccountEnabled` | `bool` |
| `IsServiceAccount` | `bool` |
| `RelatedAccounts` | `dynamic` |
| `RiskLevel` | `string` |
| `RiskLevelDetails` | `string` |
| `RiskState` | `string` |
| `SAMAccountName` | `string` |
| `TimeGenerated` | `datetime` |
| `UserAccountControl` | `dynamic` |
| `UserState` | `string` |
| `UserStateChangedOn` | `datetime` |
| `UserType` | `string` |

## Consulta inicial
```kql
IdentityInfo
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
IdentityInfo
| where TimeGenerated >= ago(24h)
| project AccountCloudSID, AccountCreationTime, AccountDisplayName, AccountDomain, AccountName, AccountObjectId, AccountSID, AccountTenantId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AccountCloudSID` | `string` |
| `AccountCreationTime` | `datetime` |
| `AccountDisplayName` | `string` |
| `AccountDomain` | `string` |
| `AccountName` | `string` |
| `AccountObjectId` | `string` |
| `AccountSID` | `string` |
| `AccountTenantId` | `string` |
| `AccountUPN` | `string` |
| `AdditionalMailAddresses` | `dynamic` |
| `Applications` | `string` |
| `AssignedRoles` | `dynamic` |
| `BlastRadius` | `string` |
| `ChangeSource` | `string` |
| `City` | `string` |
| `CompanyName` | `string` |
| `Country` | `string` |
| `DeletedDateTime` | `datetime` |
| `Department` | `string` |
| `EmployeeId` | `string` |
| `EntityRiskScore` | `dynamic` |
| `ExtensionProperty` | `dynamic` |
| `GivenName` | `string` |
| `GroupMembership` | `dynamic` |
| `InvestigationPriority` | `int` |
| `InvestigationPriorityPercentile` | `int` |
| `IsAccountEnabled` | `bool` |
| `IsMFARegistered` | `bool` |
| `IsServiceAccount` | `bool` |
| `JobTitle` | `string` |
| `LastSeenDate` | `datetime` |
| `MailAddress` | `string` |
| `Manager` | `string` |
| `OnPremisesDistinguishedName` | `string` |
| `OnPremisesExtensionAttributes` | `string` |
| `Phone` | `string` |
| `RelatedAccounts` | `dynamic` |
| `RiskLevel` | `string` |
| `RiskLevelDetails` | `string` |
| `RiskState` | `string` |
| `SAMAccountName` | `string` |
| `ServicePrincipals` | `dynamic` |
| `SourceSystem` | `string` |
| `State` | `string` |
| `StreetAddress` | `string` |
| `Surname` | `string` |
| `Tags` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `UACFlags` | `string` |
| `UserAccountControl` | `dynamic` |
| `UserState` | `string` |
| `UserStateChangedOn` | `datetime` |
| `UserType` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
