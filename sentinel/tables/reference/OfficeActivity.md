# OfficeActivity

## Objetivo de caça
atividade de auditoria Microsoft 365 para Exchange, SharePoint, Teams e outras cargas de trabalho.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `Activity` | `string` |
| `ActorIpAddress` | `string` |
| `ClientIP` | `string` |
| `ClientProcessName` | `string` |
| `Client_IPAddress` | `string` |
| `CrossMailboxOperations` | `bool` |
| `DestinationFileExtension` | `string` |
| `DestinationFileName` | `string` |
| `DestinationRelativeUrl` | `string` |
| `DestMailboxOwnerMasterAccountSid` | `string` |
| `DeviceInformation` | `string` |
| `IsManagedDevice` | `bool` |
| `LoginStatus` | `int` |
| `LogonUserDisplayName` | `string` |
| `LogonUserSid` | `string` |
| `MachineDomainInfo` | `string` |
| `MailboxOwnerMasterAccountSid` | `string` |
| `Operation` | `string` |
| `OperationProperties` | `dynamic` |
| `OperationScope` | `string` |
| `ResultStatus` | `string` |
| `SendAsUserMailboxGuid` | `string` |
| `SendAsUserSmtp` | `string` |
| `SendonBehalfOfUserMailboxGuid` | `string` |
| `SendOnBehalfOfUserSmtp` | `string` |
| `Site_Url` | `string` |
| `SourceFileExtension` | `string` |
| `SourceFileName` | `string` |
| `SourceRelativeUrl` | `string` |
| `TargetUserId` | `string` |

## Consulta inicial
```kql
OfficeActivity
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
OfficeActivity
| where TimeGenerated >= ago(24h)
| project Activity, ActorIpAddress, ClientIP, ClientProcessName, Client_IPAddress, CrossMailboxOperations, DestinationFileExtension, DestinationFileName
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AADGroupId` | `string` |
| `AADTarget` | `string` |
| `Activity` | `string` |
| `Actor` | `string` |
| `ActorContextId` | `string` |
| `ActorIpAddress` | `string` |
| `AddOnGuid` | `string` |
| `AddonName` | `string` |
| `AddOnType` | `string` |
| `AffectedItems` | `string` |
| `AppAccessContext` | `dynamic` |
| `AppDistributionMode` | `string` |
| `AppId` | `string` |
| `Application` | `string` |
| `ApplicationId` | `string` |
| `AppPoolName` | `string` |
| `ArtifactsShared` | `dynamic` |
| `Attendees` | `dynamic` |
| `AzureActiveDirectory_EventType` | `string` |
| `AzureADAppId` | `string` |
| `ChannelGuid` | `string` |
| `ChannelName` | `string` |
| `ChannelType` | `string` |
| `ChatName` | `string` |
| `ChatThreadId` | `string` |
| `Client` | `string` |
| `ClientAppId` | `string` |
| `ClientInfoString` | `string` |
| `ClientIP` | `string` |
| `ClientMachineName` | `string` |
| `ClientProcessName` | `string` |
| `ClientVersion` | `string` |
| `Client_IPAddress` | `string` |
| `CommunicationType` | `string` |
| `CrossMailboxOperations` | `bool` |
| `CustomEvent` | `string` |
| `DataCenterSecurityEventType` | `int` |
| `DestFolder` | `string` |
| `DestinationFileExtension` | `string` |
| `DestinationFileName` | `string` |
| `DestinationRelativeUrl` | `string` |
| `DestMailboxId` | `string` |
| `DestMailboxOwnerMasterAccountSid` | `string` |
| `DestMailboxOwnerSid` | `string` |
| `DestMailboxOwnerUPN` | `string` |
| `DeviceInformation` | `string` |
| `EffectiveOrganization` | `string` |
| `ElevationApprovedTime` | `datetime` |
| `ElevationApprover` | `string` |
| `ElevationDuration` | `int` |
| `ElevationRequestId` | `string` |
| `ElevationRole` | `string` |
| `ElevationTime` | `datetime` |
| `EventSource` | `string` |
| `Event_Data` | `string` |
| `ExtendedProperties` | `string` |
| `ExternalAccess` | `string` |
| `ExtraProperties` | `dynamic` |
| `Folder` | `string` |
| `Folders` | `string` |
| `GenericInfo` | `string` |
| `InternalLogonType` | `int` |
| `InterSystemsId` | `string` |
| `IntraSystemId` | `string` |
| `IsJoinedFromLobby` | `bool` |
| `IsManagedDevice` | `bool` |
| `Item` | `string` |
| `ItemName` | `string` |
| `ItemType` | `string` |
| `JoinTime` | `datetime` |
| `LeaveTime` | `datetime` |
| `ListItemUniqueId` | `string` |
| `LoginStatus` | `int` |
| `LogonUserDisplayName` | `string` |
| `LogonUserSid` | `string` |
| `Logon_Type` | `string` |
| `MachineDomainInfo` | `string` |
| `MachineId` | `string` |
| `MailboxGuid` | `string` |
| `MailboxOwnerMasterAccountSid` | `string` |
| `MailboxOwnerSid` | `string` |
| `MailboxOwnerUPN` | `string` |
| `MeetingDetailId` | `string` |
| `Members` | `dynamic` |
| `MessageId` | `string` |
| `ModifiedObjectResolvedName` | `string` |
| `ModifiedProperties` | `string` |
| `Name` | `string` |
| `NewValue` | `string` |
| `OfficeId` | `string` |
| `OfficeObjectId` | `string` |
| `OfficeTenantId` | `string` |
| `OfficeWorkload` | `string` |
| `OldValue` | `string` |
| `Operation` | `string` |
| `OperationProperties` | `dynamic` |
| `OperationScope` | `string` |
| `OrganizationId` | `string` |
| `OrganizationName` | `string` |
| `OriginatingServer` | `string` |
| `Parameters` | `string` |
| `RecordType` | `string` |
| `ResultReasonType` | `string` |
| `ResultStatus` | `string` |
| `SendAsUserMailboxGuid` | `string` |
| `SendAsUserSmtp` | `string` |
| `SendonBehalfOfUserMailboxGuid` | `string` |
| `SendOnBehalfOfUserSmtp` | `string` |
| `SensitivityLabelId` | `string` |
| `SharingType` | `string` |
| `Site_` | `string` |
| `Site_Url` | `string` |
| `SourceFileExtension` | `string` |
| `SourceFileName` | `string` |
| `SourceRecordId` | `string` |
| `SourceRelativeUrl` | `string` |
| `SourceSystem` | `string` |
| `Source_Name` | `string` |
| `SRPolicyId` | `string` |
| `SRPolicyName` | `string` |
| `SRRuleMatchDetails` | `dynamic` |
| `Start_Time` | `datetime` |
| `SupportTicketId` | `string` |
| `TabType` | `string` |
| `TargetContextId` | `string` |
| `TargetUserId` | `string` |
| `TargetUserOrGroupName` | `string` |
| `TargetUserOrGroupType` | `string` |
| `TeamGuid` | `string` |
| `TeamName` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `UniqueSharingId` | `string` |
| `UserAgent` | `string` |
| `UserDomain` | `string` |
| `UserId` | `string` |
| `UserKey` | `string` |
| `UserSharedWith` | `string` |
| `UserType` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
