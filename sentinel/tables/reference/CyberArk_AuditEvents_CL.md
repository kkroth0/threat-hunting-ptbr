# CyberArk_AuditEvents_CL

## Objetivo de caça
Eventos de auditoria CyberArk para acesso privilegiado, buscas seguras, de conta e de atividades de sessão.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `accountName` | `string` |
| `action` | `string` |
| `actionType` | `string` |
| `command` | `string` |
| `identityType` | `string` |
| `targetAccount` | `string` |
| `TimeGenerated` | `datetime` |
| `userId` | `string` |
| `username` | `string` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
CyberArk_AuditEvents_CL
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
CyberArk_AuditEvents_CL
| where TimeGenerated >= ago(24h)
| project accountName, action, actionType, command, identityType, targetAccount, TimeGenerated, userId
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `accessMethod` | `string` |
| `accountName` | `string` |
| `action` | `string` |
| `actionType` | `string` |
| `applicationCode` | `string` |
| `auditCode` | `string` |
| `auditType` | `string` |
| `cloudAssets` | `string` |
| `cloudIdentities` | `string` |
| `cloudProvider` | `string` |
| `cloudWorkspacesAndRoles` | `string` |
| `command` | `string` |
| `component` | `string` |
| `correlationId` | `string` |
| `customData` | `string` |
| `CyberArkTenantId` | `string` |
| `identityType` | `string` |
| `message` | `string` |
| `safe` | `string` |
| `serviceName` | `string` |
| `sessionId` | `string` |
| `source` | `string` |
| `target` | `string` |
| `targetAccount` | `string` |
| `targetPlatform` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `timestamp` | `int` |
| `Type` | `string` |
| `userId` | `string` |
| `username` | `string` |
| `uuid` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
