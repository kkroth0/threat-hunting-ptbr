# Heartbeat

## Objetivo de caça
Registros de pulsação do agente usados para verificar a cobertura e a integridade da coleta.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `Computer` | `string` |
| `ComputerEnvironment` | `string` |
| `ComputerIP` | `string` |
| `ComputerPrivateIPs` | `dynamic` |
| `Resource` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceProvider` | `string` |
| `ResourceType` | `string` |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
Heartbeat
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
Heartbeat
| where TimeGenerated >= ago(24h)
| project Computer, ComputerEnvironment, ComputerIP, ComputerPrivateIPs, Resource, ResourceGroup, ResourceId, ResourceProvider
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `Category` | `string` |
| `Computer` | `string` |
| `ComputerEnvironment` | `string` |
| `ComputerIP` | `string` |
| `ComputerPrivateIPs` | `dynamic` |
| `IsGatewayInstalled` | `bool` |
| `ManagementGroupName` | `string` |
| `OSMajorVersion` | `string` |
| `OSMinorVersion` | `string` |
| `OSName` | `string` |
| `OSType` | `string` |
| `RemoteIPCountry` | `string` |
| `RemoteIPLatitude` | `real` |
| `RemoteIPLongitude` | `real` |
| `Resource` | `string` |
| `ResourceGroup` | `string` |
| `ResourceId` | `string` |
| `ResourceProvider` | `string` |
| `ResourceType` | `string` |
| `SCAgentChannel` | `string` |
| `Solutions` | `string` |
| `SourceSystem` | `string` |
| `SubscriptionId` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `Version` | `string` |
| `VMUUID` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
