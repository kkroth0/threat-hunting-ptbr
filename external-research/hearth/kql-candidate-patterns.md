# HEARTH KQL Padrões Candidatos

Esses são padrões iniciais reutilizáveis Sentinel KQL para o mapeamento HEARTH Flames. Eles são candidatos, não detecções de produção. Valide a disponibilidade da tabela, os nomes dos campos, o ruído e o comportamento comercial esperado antes de promovê-los em casos de uso.

## 1. Anomalia de autenticação e revisão de força bruta
Chamas mapeadas com força bruta, spray de senha, autenticação VPN, falhas de login ou comportamento suspeito de sucesso após falha devem começar em `SigninLogs`, logs VPN/firewall em `CommonSecurityLog` e contexto de identidade em `IdentityInfo`.

```kql
let lookback = 1d;
let failureThreshold = 8;
let failures =
    SigninLogs
    | where TimeGenerated >= ago(lookback)
    | where ResultType != "0"
    | summarize
        FailedAttempts = count(),
        FailureIPs = make_set(IPAddress, 20),
        FailureApps = make_set(AppDisplayName, 20),
        LastFailure = max(TimeGenerated)
        by UserPrincipalName;
let successes =
    SigninLogs
    | where TimeGenerated >= ago(lookback)
    | where ResultType == "0"
    | summarize
        Successes = count(),
        SuccessIPs = make_set(IPAddress, 20),
        SuccessApps = make_set(AppDisplayName, 20),
        FirstSuccess = min(TimeGenerated)
        by UserPrincipalName;
failures
| where FailedAttempts >= failureThreshold
| join kind=inner successes on UserPrincipalName
| where LastFailure <= FirstSuccess
| project UserPrincipalName, FailedAttempts, Successes, FailureIPs, SuccessIPs, FailureApps, SuccessApps, LastFailure, FirstSuccess
| order by FailedAttempts desc
```

## 2. Token de identidade e abuso de OAuth
Chamas mapeadas com código de dispositivo, OAuth, roubo de token, Graph, desvio de MFA ou uso suspeito de aplicativo cliente devem começar em `SigninLogs`, `AuditLogs`, `IdentityInfo` e `OfficeActivity`.

```kql
let lookback = 7d;
SigninLogs
| where TimeGenerated >= ago(lookback)
| where ResultType == "0"
| where AuthenticationProtocol has_any ("deviceCode", "oauth", "ropc")
    or AppDisplayName has_any ("Azure CLI", "Microsoft Graph", "Office", "PowerShell")
| summarize
    FirstSeen = min(TimeGenerated),
    LastSeen = max(TimeGenerated),
    IPs = make_set(IPAddress, 20),
    Apps = make_set(AppDisplayName, 20),
    Resources = make_set(ResourceDisplayName, 20)
    by UserPrincipalName, UserAgent, Location
| order by LastSeen desc
```

## 3. Mudanças administrativas e de acesso privilegiado
Chamas mapeadas envolvendo funções administrativas, acesso privilegiado, alterações PAM, CA ou criação de conta devem começar em `AuditLogs`, `AzureActivity`, `SecurityEvent` e `CyberArk_AuditEvents_CL`.

```kql
let lookback = 7d;
union isfuzzy=true
(
    AuditLogs
    | where TimeGenerated >= ago(lookback)
    | where OperationName has_any ("role", "admin", "credential", "application", "policy")
    | project TimeGenerated, Source = "AuditLogs", Actor = tostring(InitiatedBy.user.userPrincipalName), OperationName, TargetResources, Result
),
(
    AzureActivity
    | where TimeGenerated >= ago(lookback)
    | where OperationNameValue has_any ("roleAssignments", "write", "delete")
    | project TimeGenerated, Source = "AzureActivity", Actor = Caller, OperationName = OperationNameValue, TargetResources = ResourceId, Result = ActivityStatusValue
),
(
    SecurityEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID in (4720, 4722, 4728, 4732, 4738, 4670, 4672)
    | project TimeGenerated, Source = "SecurityEvent", Actor = SubjectUserName, OperationName = tostring(EventID), TargetResources = TargetUserName, Result = Activity
)
| order by TimeGenerated desc
```

## 4. Processo de endpoint e execução de script
Chamas mapeadas envolvendo PowerShell, hosts de script, WMI/DCOM, linhas de comando suspeitas, ClickFix ou LOLBins devem começar em `SecurityEvent`, `WindowsEvent` e `TrendMicro_XDR_OAT_CL`.

```kql
let lookback = 3d;
let suspiciousTerms = dynamic(["powershell", "-enc", "frombase64string", "iex", "downloadstring", "wmic", "mshta", "rundll32", "regsvr32", "wscript", "cscript"]);
union isfuzzy=true
(
    SecurityEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID == 4688
    | extend CommandLine = tostring(CommandLine)
    | project TimeGenerated, Source = "SecurityEvent", Computer, Account, ProcessName, ParentProcessName, CommandLine
),
(
    TrendMicro_XDR_OAT_CL
    | where TimeGenerated >= ago(lookback)
    | extend CommandLine = tostring(coalesce(detail_processCmd_s, detail_objectCmd_s, detail_parentCmd_s))
    | project TimeGenerated, Source = "Trend Vision One", Computer = detail_endpointHostName_s, Account = detail_processUser_s, ProcessName = detail_processName_s, ParentProcessName = detail_parentName_s, CommandLine
)
| where CommandLine has_any (suspiciousTerms) or ProcessName has_any (suspiciousTerms)
| order by TimeGenerated desc
```

## 5. Persistência de endpoint e evasão de defesa
Chamas mapeadas envolvendo serviços, chaves de registro, IFEO, chaves de execução, drivers, tarefas agendadas, ordem de pesquisa DLL ou comprometimento da ferramenta de segurança devem começar nas tabelas de eventos de endpoint e Trend Vision One.

```kql
let lookback = 7d;
let persistenceTerms = dynamic(["CurrentVersion\\Run", "Image File Execution Options", "SilentProcessExit", "CurrentControlSet\\Services", "Scheduled Tasks", "Debugger", "MonitorProcess"]);
union isfuzzy=true
(
    SecurityEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID in (4657, 4697, 7045, 4698)
    | extend Details = tostring(EventData)
    | project TimeGenerated, Source = "SecurityEvent", Computer, Account, EventID, Details
),
(
    WindowsEvent
    | where TimeGenerated >= ago(lookback)
    | where EventID in (4657, 4697, 7045, 4698)
    | extend Details = tostring(EventData)
    | project TimeGenerated, Source = "WindowsEvent", Computer, Account = tostring(EventData.SubjectUserName), EventID, Details
),
(
    TrendMicro_XDR_OAT_CL
    | where TimeGenerated >= ago(lookback)
    | extend Details = strcat(detail_processCmd_s, " ", detail_objectRegistryKey_s, " ", detail_objectFilePath_s)
    | project TimeGenerated, Source = "Trend Vision One", Computer = detail_endpointHostName_s, Account = detail_processUser_s, EventID = detail_eventId_d, Details
)
| where Details has_any (persistenceTerms)
| order by TimeGenerated desc
```

## 6. Rede, DNS e correlação de saída
Chamas mapeadas envolvendo C2, DNS, tunelamento, resolvedores de dead-drop, tráfego de proxy, VPN ou exfiltração devem começar em `CommonSecurityLog`, `NetskopeEventsNetwork_CL`, `NetskopeEventsConnection_CL` e `Cloudflare_CL`.

```kql
let lookback = 7d;
let suspiciousDomains = dynamic(["trycloudflare.com", "workers.dev", "devtunnels.ms", "rentry.co", "telegra.ph"]);
union isfuzzy=true
(
    CommonSecurityLog
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = strcat(DeviceVendor, " ", DeviceProduct), SrcIp = SourceIP, DstIp = DestinationIP, DstPort = DestinationPort, Url = RequestURL, User = SourceUserName, Action = DeviceAction
),
(
    NetskopeEventsNetwork_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Netskope Network", SrcIp = srcip, DstIp = dstip, DstPort = dstport, Url = ur_normalized, User = user, Action = action
),
(
    Cloudflare_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Cloudflare", SrcIp = ClientIP_s, DstIp = OriginIP_s, DstPort = int(null), Url = ClientRequestURI_s, User = RequestHeaders_cf_access_user_s, Action = SecurityAction_s
)
| where Url has_any (suspiciousDomains) or Action has_any ("block", "challenge", "deny")
| summarize Events = count(), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated), Users = make_set(User, 20) by Source, SrcIp, DstIp, tostring(DstPort), Url, Action
| order by Events desc
```

## 7. Exploração de aplicativos públicos e revisão do Webshell
Chamas mapeadas envolvendo CVEs, WAF, exploração de aplicativo público, webshells, PeopleSoft, WebLogic, IIS ou comportamento de processo de servidor de aplicativo devem começar em `Cloudflare_CL`, `CommonSecurityLog`, `AzureDiagnostics`, `AppRequests`, `AppTraces` e `Syslog`.

```kql
let lookback = 7d;
let exploitTerms = dynamic(["/PSEMHUB/", "/PSIGW/", "cmd=", "whoami", "powershell", "bash", "wget", "curl", "jndi", "xml"]);
union isfuzzy=true
(
    Cloudflare_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Cloudflare", ClientIP = ClientIP_s, Uri = ClientRequestURI_s, Action = SecurityAction_s, UserAgent = ClientRequestUserAgent_s
),
(
    AppRequests
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "AppRequests", ClientIP = ClientIP, Uri = Url, Action = ResultCode, UserAgent = tostring(Properties)
),
(
    CommonSecurityLog
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = strcat(DeviceVendor, " ", DeviceProduct), ClientIP = SourceIP, Uri = RequestURL, Action = DeviceAction, UserAgent = RequestClientApplication
)
| where Uri has_any (exploitTerms) or UserAgent has_any (exploitTerms)
| order by TimeGenerated desc
```

## 8. Plano de controle de nuvem e abuso de postura
Chamas mapeadas envolvendo GCP/IAM/Azure IAM, sequestro de bucket, serviços expostos, armazenamento em nuvem ou alterações no plano de controle da nuvem devem começar em `AzureActivity`, `AzureDiagnostics`, `OrcaAlerts_CL` e quaisquer logs de provedor roteados para Sentinel.

```kql
let lookback = 14d;
union isfuzzy=true
(
    AzureActivity
    | where TimeGenerated >= ago(lookback)
    | where OperationNameValue has_any ("delete", "write", "roleAssignments", "storageAccounts", "diagnosticSettings")
    | project TimeGenerated, Source = "AzureActivity", Actor = Caller, Operation = OperationNameValue, Resource = ResourceId, Result = ActivityStatusValue
),
(
    OrcaAlerts_CL
    | where TimeGenerated >= ago(lookback)
    | where risk_level_s in~ ("critical", "high", "medium")
    | project TimeGenerated, Source = "Orca", Actor = cloud_account_name_s, Operation = alert_category_s, Resource = asset_name_s, Result = status_s
)
| order by TimeGenerated desc
```

## 9. Revisão de auditoria M365 e SaaS
Chamas mapeadas envolvendo abuso de caixa de correio, aplicativos OAuth, acesso a arquivos SaaS, regras de caixa de entrada ou uso suspeito de aplicativos devem começar nas tabelas `OfficeActivity`, `AuditLogs`, `SigninLogs` e Netskope SaaS.

```kql
let lookback = 7d;
let suspiciousOps = dynamic(["New-InboxRule", "Set-InboxRule", "Add-MailboxPermission", "Consent to application", "Add service principal"]);
union isfuzzy=true
(
    OfficeActivity
    | where TimeGenerated >= ago(lookback)
    | where Operation has_any (suspiciousOps)
    | project TimeGenerated, Source = "OfficeActivity", User = UserId, Operation, ClientIP, ObjectId, ResultStatus
),
(
    AuditLogs
    | where TimeGenerated >= ago(lookback)
    | where OperationName has_any (suspiciousOps)
    | project TimeGenerated, Source = "AuditLogs", User = tostring(InitiatedBy.user.userPrincipalName), Operation = OperationName, ClientIP = tostring(InitiatedBy.user.ipAddress), ObjectId = tostring(TargetResources), ResultStatus = Result
),
(
    NetskopeEventsApplication_CL
    | where TimeGenerated >= ago(lookback)
    | project TimeGenerated, Source = "Netskope Application", User = user, Operation = activity, ClientIP = srcip, ObjectId = object, ResultStatus = action
)
| order by TimeGenerated desc
```

## 10. IOC e varredura de indicador
Chamas mapeadas com hashes, domínios, URLs, IPs, nomes de malware ou indicadores de campanha geralmente devem começar a partir da [varredura IOC IP/domain/URL/hash](../../sentinel/kql/intel/ioc-ip-domain-url-hash-sweep.kql) existente e, em seguida, adicionar junções específicas de origem somente quando necessário.

## 11. Promoção para caso de uso
Quando uma Chama mapeada produz um sinal repetível:

1. Crie uma página a partir do [Modelo de caso de uso](../../templates/use-case-template.md).
2. Registre HEARTH ID como fonte de pesquisa externa.
3. Mantenha as tabelas Sentinel e a propagação KQL do mapeamento.
4. Adicione etapas de triagem, falsos positivos, mapeamento de entidades, gravidade e lógica de supressão.
5. Teste em Sentinel antes de ativar uma regra analítica.
