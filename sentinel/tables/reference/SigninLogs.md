# SigninLogs

## Objetivo de caça
Telemetria de login Microsoft Entra ID para autenticação, acesso condicional, risco, dispositivo, IP e buscas de acesso a aplicativos.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `AuthenticationAppDeviceDetails` | `string` |
| `AuthenticationProcessingDetails` | `string` |
| `AuthenticatorAppLocation` | `string` |
| `ConditionalAccessStatus` | `string` |
| `DeviceDetail` | `dynamic` |
| `GlobalSecureAccessIpAddress` | `string` |
| `Identity` | `string` |
| `IPAddress` | `string` |
| `IPAddressFromResourceProvider` | `string` |
| `IsRisky` | `bool` |
| `Location` | `string` |
| `LocationDetails` | `dynamic` |
| `NetworkLocationDetails` | `string` |
| `OperationName` | `string` |
| `OperationVersion` | `string` |
| `ProcessingTimeInMilliseconds` | `string` |
| `Resource` | `string` |
| `ResourceDisplayName` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceIdentity` | `string` |
| `ResourceOwnerTenantId` | `string` |
| `ResourceProvider` | `string` |
| `ResourceServicePrincipalId` | `string` |
| `ResourceTenantId` | `string` |
| `RiskDetail` | `string` |
| `RiskEventTypes` | `string` |
| `RiskEventTypes_V2` | `string` |
| `RiskLevel` | `string` |
| `RiskLevelAggregated` | `string` |

## Consulta inicial
```kql
SigninLogs
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
SigninLogs
| where TimeGenerated >= ago(24h)
| project AuthenticationAppDeviceDetails, AuthenticationProcessingDetails, AuthenticatorAppLocation, ConditionalAccessStatus, DeviceDetail, GlobalSecureAccessIpAddress, Identity, IPAddress
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AADTenantId` | `string` |
| `Agent` | `dynamic` |
| `AlternateSignInName` | `string` |
| `AppDisplayName` | `string` |
| `AppId` | `string` |
| `AppliedConditionalAccessPolicies` | `string` |
| `AppliedEventListeners` | `dynamic` |
| `AppOwnerTenantId` | `string` |
| `AuthenticationAppDeviceDetails` | `string` |
| `AuthenticationAppPolicyEvaluationDetails` | `string` |
| `AuthenticationContextClassReferences` | `string` |
| `AuthenticationDetails` | `string` |
| `AuthenticationMethodsUsed` | `string` |
| `AuthenticationProcessingDetails` | `string` |
| `AuthenticationProtocol` | `string` |
| `AuthenticationRequirement` | `string` |
| `AuthenticationRequirementPolicies` | `string` |
| `AuthenticatorAppLocation` | `string` |
| `AutonomousSystemNumber` | `string` |
| `Category` | `string` |
| `ClientAppUsed` | `string` |
| `ClientCredentialType` | `string` |
| `ConditionalAccessAudiences` | `string` |
| `ConditionalAccessPolicies` | `dynamic` |
| `ConditionalAccessStatus` | `string` |
| `CorrelationId` | `string` |
| `CreatedDateTime` | `datetime` |
| `CrossTenantAccessType` | `string` |
| `DeviceDetail` | `dynamic` |
| `DurationMs` | `long` |
| `FederatedCredentialId` | `string` |
| `FlaggedForReview` | `bool` |
| `GlobalSecureAccessIpAddress` | `string` |
| `HomeTenantId` | `string` |
| `HomeTenantName` | `string` |
| `Id` | `string` |
| `Identity` | `string` |
| `IncomingTokenType` | `string` |
| `IPAddress` | `string` |
| `IPAddressFromResourceProvider` | `string` |
| `IsInteractive` | `bool` |
| `IsRisky` | `bool` |
| `IsTenantRestricted` | `bool` |
| `IsThroughGlobalSecureAccess` | `bool` |
| `Level` | `string` |
| `Location` | `string` |
| `LocationDetails` | `dynamic` |
| `MfaDetail` | `dynamic` |
| `NetworkLocationDetails` | `string` |
| `OperationName` | `string` |
| `OperationVersion` | `string` |
| `OriginalRequestId` | `string` |
| `OriginalTransferMethod` | `string` |
| `ProcessingTimeInMilliseconds` | `string` |
| `Resource` | `string` |
| `ResourceDisplayName` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceIdentity` | `string` |
| `ResourceOwnerTenantId` | `string` |
| `ResourceProvider` | `string` |
| `ResourceServicePrincipalId` | `string` |
| `ResourceTenantId` | `string` |
| `ResultDescription` | `string` |
| `ResultSignature` | `string` |
| `ResultType` | `string` |
| `RiskDetail` | `string` |
| `RiskEventTypes` | `string` |
| `RiskEventTypes_V2` | `string` |
| `RiskLevel` | `string` |
| `RiskLevelAggregated` | `string` |
| `RiskLevelDuringSignIn` | `string` |
| `RiskState` | `string` |
| `ServicePrincipalId` | `string` |
| `ServicePrincipalName` | `string` |
| `SessionId` | `string` |
| `SessionLifetimePolicies` | `string` |
| `SignInIdentifier` | `string` |
| `SignInIdentifierType` | `string` |
| `SourceAppClientId` | `string` |
| `SourceSystem` | `string` |
| `Status` | `dynamic` |
| `TimeGenerated` | `datetime` |
| `TokenIssuerName` | `string` |
| `TokenIssuerType` | `string` |
| `TokenProtectionStatusDetails` | `dynamic` |
| `Type` | `string` |
| `UniqueTokenIdentifier` | `string` |
| `UserAgent` | `string` |
| `UserDisplayName` | `string` |
| `UserId` | `string` |
| `UserPrincipalName` | `string` |
| `UserType` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
