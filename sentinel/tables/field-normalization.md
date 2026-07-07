# Normalização de campo

Ferramentas diferentes usam nomes de campo diferentes para a mesma entidade de busca. Normalize os campos dentro de KQL antes de unir ou resumir.

## Mapeamento de entidade
| Entidade | Campos Comuns |
| --- | --- |
| Usuário | `UserPrincipalName`, `userPrincipalName`, `UserId`, `user`, `Account`, `AccountName`, `SubjectUserName`, `TargetUserName`, `username`, `UserAccountName_s` |
| Anfitrião | `Computer`, `HostHostName_s`, `hostname`, `asset_hostname_s`, `detail_endpointHostName_s`, `DeviceName`, `SourceHostName`, `DestinationHostName` |
| Fonte IP | `IPAddress`, `ClientIP_s`, `SourceIP`, `srcip`, `userip`, `ClientIP`, `IpAddress`, `detail_src_s` |
| Destino IP | `DestinationIP`, `dstip`, `OriginIP_s`, `detail_dst_s`, `IPAddress` |
| URL ou Host | `RequestURL`, `ClientRequestURI_s`, `url`, `ur_normalized`, `URL_s`, `findings_PublicUrl_s`, `ClientRequestHost_s`, `domain`, `dsthost` |
| Hash de arquivo | `FileHash`, `sha256`, `md5`, `FileHashValue_s`, `detail_fileHashSha256_s`, `detail_objectFileHashSha256_s`, `findings_Sha256_s` |
| Ação | `DeviceAction`, `SimplifiedDeviceAction`, `SecurityAction_s`, `action`, `detail_act_s`, `Activity`, `OperationName` |
| Gravidade | `Severity`, `AlertSeverity`, `severity`, `severity_s`, `risk_level_s`, `LogSeverity`, `ThreatSeverity` |

## Padrão KQL
```kql
<TableName>
| extend
    NormalizedUser = coalesce(UserPrincipalName, userPrincipalName, UserId, user, Account),
    NormalizedHost = coalesce(Computer, HostHostName_s, hostname),
    NormalizedSourceIp = coalesce(IPAddress, ClientIP_s, SourceIP, srcip, userip),
    NormalizedDestinationIp = coalesce(DestinationIP, dstip, OriginIP_s),
    NormalizedAction = coalesce(DeviceAction, SecurityAction_s, action, Activity),
    NormalizedSeverity = coalesce(Severity, AlertSeverity, severity, severity_s, risk_level_s)
```

## Notas
- Normalize apenas os campos necessários para a caça.
- Mantenha os campos brutos na projeção final para que um analista possa retornar ao evento original do fornecedor.
- Prefira `column_ifexists()` ao gravar analisadores compartilhados em tabelas personalizadas opcionais.
