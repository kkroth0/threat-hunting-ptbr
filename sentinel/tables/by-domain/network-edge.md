# Rede, Borda e SASE

Firewall, proxy, WAF, DNS, web, SASE e telemetria de borda normalizados para buscas de rede.

## Tabelas
| Tabela | Campos | Objetivo de caça |
| --- | ---: | --- |
| [CommonSecurityLog](../reference/CommonSecurityLog.md) | 163 | Telemetria de segurança estilo CEF comumente usada para firewalls, dispositivos de segurança de rede e logs de proxy. |
| [Cloudflare_CL](../reference/Cloudflare_CL.md) | 128 | Tabela de log personalizada Cloudflare para WAF, edge, bot, request, origin e buscas de ação de segurança. |
| [NetskopeAlerts_CL](../reference/NetskopeAlerts_CL.md) | 207 | Tabela personalizada Netskope usada para SASE, CASB, web, DLP, aplicativo e busca de rede. |
| [NetskopeEventsApplication_CL](../reference/NetskopeEventsApplication_CL.md) | 152 | Tabela personalizada Netskope usada para SASE, CASB, web, DLP, aplicativo e busca de rede. |
| [NetskopeEventsAudit_CL](../reference/NetskopeEventsAudit_CL.md) | 19 | Tabela personalizada Netskope usada para SASE, CASB, web, DLP, aplicativo e busca de rede. |
| [NetskopeEventsConnection_CL](../reference/NetskopeEventsConnection_CL.md) | 92 | Tabela personalizada Netskope usada para SASE, CASB, web, DLP, aplicativo e busca de rede. |
| [NetskopeEventsNetwork_CL](../reference/NetskopeEventsNetwork_CL.md) | 73 | Tabela personalizada Netskope usada para SASE, CASB, web, DLP, aplicativo e busca de rede. |
| [NetskopeEventsPage_CL](../reference/NetskopeEventsPage_CL.md) | 92 | Tabela personalizada Netskope usada para SASE, CASB, web, DLP, aplicativo e busca de rede. |

## Perguntas comuns
- Que pergunta de segurança esta tabela pode responder?
- Qual entidade ele pode identificar: usuário, host, IP, URL, hash, recurso de nuvem ou incidente?
- A qual outra tabela deveria ser associada para fins de contexto?
- Qual cadência de caça o utiliza: Diariamente, Semanalmente, Intel ou Mensalmente?
