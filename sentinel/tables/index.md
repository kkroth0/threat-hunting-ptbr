# Catálogo de tabelas Sentinel

Este catálogo foi gerado a partir do esquema Microsoft Sentinel/Log Analytics exportado para `references/sentinel/logmanagement-schema.txt`.

A fonte continha 49 entradas de tabela. Seções duplicadas foram recolhidas para: CommonSecurityLog, SecurityAlert, SecurityEvent.

## Visualizações de domínio
- [Identidade e acesso](by-domain/identity-access.md): autenticação, atividade de auditoria Entra ID, UEBA, análise de pares, acesso privilegiado e atividade do usuário M365.
- [Endpoint e sistemas operacionais](by-domain/endpoint-os.md): Windows, Linux, integridade do agente, processo, logon, serviço, script e telemetria de host.
- [Rede, Edge e SASE](by-domain/network-edge.md): Firewall, proxy, WAF, DNS, web, SASE e telemetria de borda normalizados para buscas de rede.
- [Nuvem e Postura](by-domain/cloud-posture.md): plano de controle Azure, diagnóstico de nuvem, postura de segurança em nuvem, risco de carga de trabalho e telemetria de exposição.
- [Detecções, casos e Intel](by-domain/detections-cases-intel.md): Sentinel detecções, incidentes, anomalias, listas de observação, integridade, auditoria e inteligência de ameaças.
- [Monitoramento de aplicativos e plataformas](by-domain/application-monitoring.md): Application Insights, aplicativos de funções, auditoria de consulta Log Analytics, uso de ingestão e telemetria de aplicativos.

## Ferramenta para mapa de tabela
- [Mapa da tabela de ferramentas](tool-table-map.md)
- [Normalização de campo](field-normalization.md)

## Referência de tabela
| Tabela | Domínio | Campos |
| --- | --- | ---: |
| [AppDependencies](reference/AppDependencies.md) | Monitoramento de Aplicativos e Plataformas | 43 |
| [AppExceptions](reference/AppExceptions.md) | Monitoramento de Aplicativos e Plataformas | 49 |
| [AppMetrics](reference/AppMetrics.md) | Monitoramento de Aplicativos e Plataformas | 36 |
| [AppPerformanceCounters](reference/AppPerformanceCounters.md) | Monitoramento de Aplicativos e Plataformas | 36 |
| [AppRequests](reference/AppRequests.md) | Monitoramento de Aplicativos e Plataformas | 42 |
| [AppSystemEvents](reference/AppSystemEvents.md) | Monitoramento de Aplicativos e Plataformas | 12 |
| [AppTraces](reference/AppTraces.md) | Monitoramento de Aplicativos e Plataformas | 37 |
| [AuditLogs](reference/AuditLogs.md) | Identidade e Acesso | 31 |
| [AzureActivity](reference/AzureActivity.md) | Nuvem e Postura | 37 |
| [AzureDiagnostics](reference/AzureDiagnostics.md) | Nuvem e Postura | 52 |
| [FunctionAppLogs](reference/FunctionAppLogs.md) | Monitoramento de Aplicativos e Plataformas | 26 |
| [Heartbeat](reference/Heartbeat.md) | Endpoint e sistemas operacionais | 31 |
| [LAQueryLogs](reference/LAQueryLogs.md) | Monitoramento de Aplicativos e Plataformas | 35 |
| [SigninLogs](reference/SigninLogs.md) | Identidade e Acesso | 95 |
| [Syslog](reference/Syslog.md) | Endpoint e sistemas operacionais | 17 |
| [Usage](reference/Usage.md) | Monitoramento de Aplicativos e Plataformas | 23 |
| [Anomalies](reference/Anomalies.md) | Detecções, casos e informações | 38 |
| [CommonSecurityLog](reference/CommonSecurityLog.md) | Rede, Borda e SASE | 163 |
| [OfficeActivity](reference/OfficeActivity.md) | Identidade e Acesso | 144 |
| [SecurityAlert](reference/SecurityAlert.md) | Detecções, casos e informações | 35 |
| [SecurityEvent](reference/SecurityEvent.md) | Endpoint e sistemas operacionais | 228 |
| [SecurityIncident](reference/SecurityIncident.md) | Detecções, casos e informações | 33 |
| [SentinelAudit](reference/SentinelAudit.md) | Detecções, casos e informações | 16 |
| [SentinelHealth](reference/SentinelHealth.md) | Detecções, casos e informações | 17 |
| [ThreatIntelIndicators](reference/ThreatIntelIndicators.md) | Detecções, casos e informações | 26 |
| [Watchlist](reference/Watchlist.md) | Detecções, casos e informações | 30 |
| [WindowsEvent](reference/WindowsEvent.md) | Endpoint e sistemas operacionais | 26 |
| [BehaviorAnalytics](reference/BehaviorAnalytics.md) | Identidade e Acesso | 33 |
| [IdentityInfo](reference/IdentityInfo.md) | Identidade e Acesso | 57 |
| [UserPeerAnalytics](reference/UserPeerAnalytics.md) | Identidade e Acesso | 16 |
| [AMAAgentHealth_CL](reference/AMAAgentHealth_CL.md) | Endpoint e sistemas operacionais | 8 |
| [Cloudflare_CL](reference/Cloudflare_CL.md) | Rede, Borda e SASE | 128 |
| [CyberArk_AuditEvents_CL](reference/CyberArk_AuditEvents_CL.md) | Identidade e Acesso | 36 |
| [NetskopeAlerts_CL](reference/NetskopeAlerts_CL.md) | Rede, Borda e SASE | 207 |
| [NetskopeEventsApplication_CL](reference/NetskopeEventsApplication_CL.md) | Rede, Borda e SASE | 152 |
| [NetskopeEventsAudit_CL](reference/NetskopeEventsAudit_CL.md) | Rede, Borda e SASE | 19 |
| [NetskopeEventsConnection_CL](reference/NetskopeEventsConnection_CL.md) | Rede, Borda e SASE | 92 |
| [NetskopeEventsNetwork_CL](reference/NetskopeEventsNetwork_CL.md) | Rede, Borda e SASE | 73 |
| [NetskopeEventsPage_CL](reference/NetskopeEventsPage_CL.md) | Rede, Borda e SASE | 92 |
| [OrcaAlerts_CL](reference/OrcaAlerts_CL.md) | Nuvem e Postura | 436 |
| [SAP_CL](reference/SAP_CL.md) | Nuvem e Postura | 8 |
| [TrendMicro_XDR_Health_Check_CL](reference/TrendMicro_XDR_Health_Check_CL.md) | Endpoint e sistemas operacionais | 13 |
| [TrendMicro_XDR_OAT_CL](reference/TrendMicro_XDR_OAT_CL.md) | Endpoint e sistemas operacionais | 387 |
| [TrendMicro_XDR_OAT_Health_Check_CL](reference/TrendMicro_XDR_OAT_Health_Check_CL.md) | Endpoint e sistemas operacionais | 12 |
| [TrendMicro_XDR_WORKBENCH_CL](reference/TrendMicro_XDR_WORKBENCH_CL.md) | Endpoint e sistemas operacionais | 44 |
