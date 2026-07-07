# UserPeerAnalytics

## Objetivo de caça
Análise de grupos de pares de usuários para análise de anomalias de identidade e valores discrepantes.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `PeerUserId` | `string` |
| `PeerUserName` | `string` |
| `PeerUserPrincipalName` | `string` |
| `TimeGenerated` | `datetime` |
| `UserId` | `string` |
| `UserName` | `string` |
| `UserPrincipalName` | `string` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
UserPeerAnalytics
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
UserPeerAnalytics
| where TimeGenerated >= ago(24h)
| project PeerUserId, PeerUserName, PeerUserPrincipalName, TimeGenerated, UserId, UserName, UserPrincipalName, _ResourceId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AADTenantId` | `string` |
| `PeerUserId` | `string` |
| `PeerUserName` | `string` |
| `PeerUserPrincipalName` | `string` |
| `Rank` | `int` |
| `SourceSystem` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `UserId` | `string` |
| `UserName` | `string` |
| `UserPrincipalName` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
