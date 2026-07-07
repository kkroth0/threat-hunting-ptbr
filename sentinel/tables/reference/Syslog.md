# Syslog

## Objetivo de caça
Tabela Sentinel/Log Analytics disponível para busca e correlação.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `CollectorHostName` | `string` |
| `Computer` | `string` |
| `HostIP` | `string` |
| `HostName` | `string` |
| `ProcessID` | `int` |
| `ProcessName` | `string` |
| `SeverityLevel` | `string` |
| `TimeGenerated` | `datetime` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
Syslog
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
Syslog
| where TimeGenerated >= ago(24h)
| project CollectorHostName, Computer, HostIP, HostName, ProcessID, ProcessName, SeverityLevel, TimeGenerated
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `CollectorHostName` | `string` |
| `Computer` | `string` |
| `EventTime` | `datetime` |
| `Facility` | `string` |
| `HostIP` | `string` |
| `HostName` | `string` |
| `ProcessID` | `int` |
| `ProcessName` | `string` |
| `SeverityLevel` | `string` |
| `SourceSystem` | `string` |
| `SyslogMessage` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
