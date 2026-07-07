# TrendMicro_XDR_WORKBENCH_CL

## Objetivo de caça
Tabela customizada Trend Vision One usada para integridade, detecção ou busca no ambiente de trabalho endpoint/XDR.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `alertProvider_s` | `string` |
| `alertTriggerTimestamp_t` | `datetime` |
| `Computer` | `string` |
| `DomainName_s` | `string` |
| `FileDirectory_s` | `string` |
| `FileHashValue_s` | `string` |
| `FileName_s` | `string` |
| `HostHostName_s` | `string` |
| `investigationStatus_s` | `string` |
| `IPAddress` | `string` |
| `ProcessCommandLine_s` | `string` |
| `severity_s` | `string` |
| `TimeGenerated` | `datetime` |
| `URL_s` | `string` |
| `UserAccountName_s` | `string` |
| `UserAccountNTDomain_s` | `string` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
TrendMicro_XDR_WORKBENCH_CL
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
TrendMicro_XDR_WORKBENCH_CL
| where TimeGenerated >= ago(24h)
| project alertProvider_s, alertTriggerTimestamp_t, Computer, DomainName_s, FileDirectory_s, FileHashValue_s, FileName_s, HostHostName_s
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `alertProvider_s` | `string` |
| `alertTriggerTimestamp_t` | `datetime` |
| `Computer` | `string` |
| `createdTime_t` | `datetime` |
| `description_s` | `string` |
| `DomainName_s` | `string` |
| `FileDirectory_s` | `string` |
| `FileHashValue_s` | `string` |
| `FileName_s` | `string` |
| `HostHostName_s` | `string` |
| `impactScope_over_size_b` | `bool` |
| `impactScope_s` | `string` |
| `impactScope_Summary_s` | `string` |
| `indicators_over_size_b` | `bool` |
| `indicators_s` | `string` |
| `investigationStatus_s` | `string` |
| `IPAddress` | `string` |
| `MalwareName_s` | `string` |
| `matchedRules_s` | `string` |
| `modelId_g` | `string` |
| `modelId_s` | `string` |
| `model_s` | `string` |
| `priorityScore_d` | `real` |
| `ProcessCommandLine_s` | `string` |
| `RawData` | `string` |
| `RegistryKey_s` | `string` |
| `RegistryValueName_s` | `string` |
| `RegistryValue_s` | `string` |
| `severity_s` | `string` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `updatedTime_t` | `datetime` |
| `URL_s` | `string` |
| `UserAccountName_s` | `string` |
| `UserAccountNTDomain_s` | `string` |
| `workbenchCompleteTimestamp_t` | `datetime` |
| `workbenchId_s` | `string` |
| `workbenchLink_s` | `string` |
| `workbenchName_s` | `string` |
| `xdrCustomerID_g` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
