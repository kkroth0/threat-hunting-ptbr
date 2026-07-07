# KQL Library

Esta pasta armazena KQL reutilizáveis para o processo de busca. Cada consulta é mapeada para uma página de busca e para uma cadência recorrente.

## HEARTH Iniciantes
- [HEARTH KQL Starters](hearth/README.md): um candidato inicial KQL gerado por chama HEARTH, mapeado para as tabelas Sentinel disponíveis nesta biblioteca.

## Consultas
| Consulta | Cadência | Tabelas Principais |
| --- | --- | --- |
| [Falhas de identidade seguidas de sucesso](daily/identity-failures-followed-by-success.kql) | Caça Diária | SigninLogs |
| [Alertas e incidentes de alta gravidade](daily/high-severity-alerts-and-incidents.kql) | Caça Diária | SecurityIncident, SecurityAlert, TrendMicro_XDR_WORKBENCH_CL, OrcaAlerts_CL, NetskopeAlerts_CL |
| [Ponto final suspeito PowerShell](daily/endpoint-suspicious-powershell.kql) | Caça Diária | SecurityEvent, WindowsEvent, TrendMicro_XDR_OAT_CL |
| [Rede WAF e blocos de firewall](daily/network-waf-and-firewall-blocks.kql) | Caça Diária | CommonSecurityLog, Cloudflare_CL, NetskopeEventsNetwork_CL |
| [Saúde da fonte de dados](daily/data-source-health.kql) | Caça Diária | Heartbeat, SentinelHealth, AMAAgentHealth_CL, TrendMicro_XDR_Health_Check_CL, TrendMicro_XDR_OAT_Health_Check_CL |
| [Novas alterações de administrador ou função](weekly/new-admin-or-role-changes.kql) | Caça Semanal | AuditLogs, AzureActivity, CyberArk_AuditEvents_CL |
| [Postura de risco na nuvem](weekly/cloud-risk-posture.kql) | Caça Semanal | OrcaAlerts_CL, AzureActivity, AzureDiagnostics |
| [Acesso raro a aplicativos e agentes de usuário](weekly/rare-app-and-user-agent-access.kql) | Caça Semanal | SigninLogs, OfficeActivity, NetskopeEventsApplication_CL |
| [Principais saídas e tráfego negado](weekly/top-egress-and-denied-traffic.kql) | Caça Semanal | CommonSecurityLog, NetskopeEventsNetwork_CL, Cloudflare_CL |
| [IOC IP Domínio URL Varredura de hash](intel/ioc-ip-domain-url-hash-sweep.kql) | Caça à Intel | ThreatIntelIndicators, CommonSecurityLog, Cloudflare_CL, NetskopeAlerts_CL, NetskopeEventsApplication_CL, NetskopeEventsNetwork_CL, TrendMicro_XDR_OAT_CL, TrendMicro_XDR_WORKBENCH_CL, OrcaAlerts_CL |
| [Tendência de mapeamento MITRE](intel/trend-mitre-mapping-hunt.kql) | Caça à Intel | TrendMicro_XDR_OAT_CL, SecurityAlert |
| [Varredura de exposição à nuvem de alto risco](intel/high-risk-cloud-exposure-sweep.kql) | Caça à Intel | OrcaAlerts_CL, AzureActivity, Cloudflare_CL |
| [Revisão de cobertura e ingestão](monthly/coverage-and-ingestion-review.kql) | Caça Mensal | Usage, Heartbeat, SentinelHealth |
| [Regra de análise e qualidade do incidente](monthly/analytics-rule-and-incident-quality.kql) | Caça Mensal | SecurityIncident, SecurityAlert, SentinelAudit |
| [Revisão da linha de base de identidade](monthly/identity-baseline-review.kql) | Caça Mensal | IdentityInfo, SigninLogs, AuditLogs |
| [Custo de registro e volume faturável](monthly/log-cost-and-billable-volume.kql) | Caça Mensal | SigninLogs, AuditLogs, SecurityEvent, WindowsEvent, CommonSecurityLog, Cloudflare_CL, NetskopeAlerts_CL, NetskopeEventsApplication_CL, NetskopeEventsConnection_CL, NetskopeEventsNetwork_CL, NetskopeEventsPage_CL, OrcaAlerts_CL, TrendMicro_XDR_OAT_CL, TrendMicro_XDR_WORKBENCH_CL |

## Padrão de Trabalho
1. Confirme se a tabela existe e está recebendo dados.
2. Execute a consulta com o lookback padrão.
3. Ajuste os limites para sua linha de base.
4. Salve as descobertas confirmadas na página de busca correspondente.
5. Promova lógica repetida de alto valor em uma regra analítica ou pasta de trabalho.
