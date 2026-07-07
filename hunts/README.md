# Biblioteca de caça

As páginas de caça são o principal produto deste repositório. Cada página conecta um cenário a tabelas Sentinel, ferramentas, KQL, fluxo de trabalho do analista e saída esperada.

## Índice de caça
| Caça | Cadência | Tabelas Principais |
| --- | --- | --- |
| [Falhas de identidade seguidas de sucesso](daily/identity-failures-followed-by-success.md) | Caça Diária | SigninLogs |
| [Alertas e incidentes de alta gravidade](daily/high-severity-alerts-and-incidents.md) | Caça Diária | SecurityIncident, SecurityAlert, TrendMicro_XDR_WORKBENCH_CL, OrcaAlerts_CL, NetskopeAlerts_CL |
| [Ponto final suspeito PowerShell](daily/endpoint-suspicious-powershell.md) | Caça Diária | SecurityEvent, WindowsEvent, TrendMicro_XDR_OAT_CL |
| [Rede WAF e blocos de firewall](daily/network-waf-and-firewall-blocks.md) | Caça Diária | CommonSecurityLog, Cloudflare_CL, NetskopeEventsNetwork_CL |
| [Saúde da fonte de dados](daily/data-source-health.md) | Caça Diária | Heartbeat, SentinelHealth, AMAAgentHealth_CL, TrendMicro_XDR_Health_Check_CL, TrendMicro_XDR_OAT_Health_Check_CL |
| [Novas alterações de administrador ou função](weekly/new-admin-or-role-changes.md) | Caça Semanal | AuditLogs, AzureActivity, CyberArk_AuditEvents_CL |
| [Postura de risco na nuvem](weekly/cloud-risk-posture.md) | Caça Semanal | OrcaAlerts_CL, AzureActivity, AzureDiagnostics |
| [Acesso raro a aplicativos e agentes de usuário](weekly/rare-app-and-user-agent-access.md) | Caça Semanal | SigninLogs, OfficeActivity, NetskopeEventsApplication_CL |
| [Principais saídas e tráfego negado](weekly/top-egress-and-denied-traffic.md) | Caça Semanal | CommonSecurityLog, NetskopeEventsNetwork_CL, Cloudflare_CL |
| [IOC IP Domínio URL Varredura de hash](intel/ioc-ip-domain-url-hash-sweep.md) | Caça à Intel | ThreatIntelIndicators, CommonSecurityLog, Cloudflare_CL, NetskopeAlerts_CL, NetskopeEventsApplication_CL, NetskopeEventsNetwork_CL, TrendMicro_XDR_OAT_CL, TrendMicro_XDR_WORKBENCH_CL, OrcaAlerts_CL |
| [Tendência de mapeamento MITRE](intel/trend-mitre-mapping-hunt.md) | Caça à Intel | TrendMicro_XDR_OAT_CL, SecurityAlert |
| [Varredura de exposição à nuvem de alto risco](intel/high-risk-cloud-exposure-sweep.md) | Caça à Intel | OrcaAlerts_CL, AzureActivity, Cloudflare_CL |
| [Revisão de cobertura e ingestão](monthly/coverage-and-ingestion-review.md) | Caça Mensal | Usage, Heartbeat, SentinelHealth |
| [Regra de análise e qualidade do incidente](monthly/analytics-rule-and-incident-quality.md) | Caça Mensal | SecurityIncident, SecurityAlert, SentinelAudit |
| [Revisão da linha de base de identidade](monthly/identity-baseline-review.md) | Caça Mensal | IdentityInfo, SigninLogs, AuditLogs |
| [Custo de registro e volume faturável](monthly/log-cost-and-billable-volume.md) | Caça Mensal | SigninLogs, AuditLogs, SecurityEvent, WindowsEvent, CommonSecurityLog, Cloudflare_CL, NetskopeAlerts_CL, NetskopeEventsApplication_CL, NetskopeEventsConnection_CL, NetskopeEventsNetwork_CL, NetskopeEventsPage_CL, OrcaAlerts_CL, TrendMicro_XDR_OAT_CL, TrendMicro_XDR_WORKBENCH_CL |

## Cadências
- [Caça Diária](daily/README.md)
- [Caça Semanal](weekly/README.md)
- [Caça à Intel](intel/README.md)
- [Caça Mensal](monthly/README.md)
