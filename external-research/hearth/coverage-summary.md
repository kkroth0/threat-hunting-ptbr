# HEARTH Resumo da cobertura de chamas

Total de chamas mapeadas: 221

## Domínios
| Item | Contagem |
| --- | --- |
| Ponto final e OS | 200 |
| Identidade e Acesso | 144 |
| Borda de rede e SASE | 120 |
| Intel e detecções de ameaças | 119 |
| Nuvem e Postura | 74 |
| Borda da Web e de Aplicativos | 68 |
| Linux e Servidor | 54 |
| M365 e SaaS | 38 |
| Acesso Privilegiado | 17 |

## Tabelas Sentinel
| Item | Contagem |
| --- | --- |
| SecurityEvent | 195 |
| WindowsEvent | 191 |
| TrendMicro_XDR_OAT_CL | 188 |
| TrendMicro_XDR_WORKBENCH_CL | 186 |
| CommonSecurityLog | 154 |
| AuditLogs | 140 |
| SigninLogs | 136 |
| IdentityInfo | 119 |
| NetskopeEventsNetwork_CL | 108 |
| Cloudflare_CL | 98 |
| ThreatIntelIndicators | 98 |
| NetskopeEventsConnection_CL | 93 |
| Watchlist | 91 |
| BehaviorAnalytics | 89 |
| SecurityAlert | 88 |
| AzureDiagnostics | 88 |
| UserPeerAnalytics | 85 |
| Syslog | 69 |
| NetskopeAlerts_CL | 63 |
| SecurityIncident | 57 |
| Anomalies | 51 |
| AzureActivity | 41 |
| OrcaAlerts_CL | 40 |
| AppRequests | 38 |
| Heartbeat | 36 |
| AppTraces | 36 |
| OfficeActivity | 24 |
| NetskopeEventsApplication_CL | 15 |
| NetskopeEventsAudit_CL | 12 |
| NetskopeEventsPage_CL | 9 |
| CyberArk_AuditEvents_CL | 5 |

## Cadência
| Item | Contagem |
| --- | --- |
| Caça à Intel | 114 |
| Caça Semanal | 70 |
| Caça Diária | 37 |

## Status de cobertura
| Item | Contagem |
| --- | --- |
| Starter KQL - validar em Sentinel | 198 |
| Starter - validar telemetria SaaS | 7 |
| Starter - validar telemetria Linux | 7 |
| Parcial - ajuste personalizado necessário | 5 |
| Starter - validar telemetria em nuvem | 4 |

## Prioridade
| Item | Contagem |
| --- | --- |
| P2 | 114 |
| P3 | 76 |
| P1 | 25 |
| P4 | 6 |

## KQL Padrões Candidatos
| Item | Contagem |
| --- | --- |
| Persistência de endpoint e cadeia de evasão de defesa | 83 |
| Script suspeito e execução de comandos | 32 |
| Exploração de aplicativos públicos e revisão de webshell | 27 |
| Correlação de abuso de identidade token/OAuth | 22 |
| Correlação de anomalia de rede, DNS e saída | 19 |
| IOC e varredura do indicador | 12 |
| Anomalia de autenticação e revisão de força bruta | 6 |
| auditoria SaaS/M365 e revisão da atividade da caixa de correio | 6 |
| Linux syslog/auditd processo e revisão de arquivo | 6 |
| Correlação Sentinel específica da hipótese | 5 |
| Revisão do plano de controle da nuvem e do abuso de postura | 3 |

## LATAM Relevância
| Item | Contagem |
| --- | --- |
| Padrão - mantenha para cobertura global | 147 |
| Médio - padrão comum de ameaça empresarial LATAM | 71 |
| Alta - atividades bancárias regionais, nacionais ou específicas de LATAM | 3 |

## Principais técnicas MITRE
| Item | Contagem |
| --- | --- |
| T1059.001 | 9 |
| T1562.001 | 9 |
| T1204.002 | 9 |
| T1574.002 | 8 |
| T1219 | 7 |
| T1105 | 7 |
| T1195.002 | 7 |
| T1055 | 6 |
| T1190 | 6 |
| T1036.005 | 5 |
| T1555 | 5 |
| T1021 | 4 |
| T1572 | 4 |
| T1218 | 4 |
| T1195.001 | 4 |
| T1552.001 | 4 |
| T1053.005 | 4 |
| T1505.003 | 4 |
| T1649 | 4 |
| T1059 | 3 |
| T1068 | 3 |
| T1566.001 | 3 |
| T1005 | 3 |
| T1059.002 | 3 |
| T1027 | 3 |
| T1059.004 | 3 |
| T1059.007 | 3 |
| T1486 | 3 |
| T1003.003 | 3 |
| T1574.001 | 3 |
| T1078.004 | 3 |
| T1550 | 3 |
| T1071.001 | 3 |
| T1110 | 2 |
| T1560.001 | 2 |
| T1218.005 | 2 |
| T1048 | 2 |
| T1071.004 | 2 |
| T1112 | 2 |
| T1078 | 2 |
