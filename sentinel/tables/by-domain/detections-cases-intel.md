# Detecções, casos e informações

Sentinel detecções, incidentes, anomalias, listas de observação, integridade, auditoria e inteligência de ameaças.

## Tabelas
| Tabela | Campos | Objetivo de caça |
| --- | ---: | --- |
| [SecurityAlert](../reference/SecurityAlert.md) | 35 | Registros de alerta produzidos pela Microsoft e produtos de segurança conectados. |
| [SecurityIncident](../reference/SecurityIncident.md) | 33 | registros de incidentes Microsoft Sentinel para gerenciamento de casos, qualidade de triagem e revisão do ciclo de vida de incidentes. |
| [Anomalies](../reference/Anomalies.md) | 38 | registros de Anomalies Sentinel para análise de comportamento e detecção. |
| [SentinelAudit](../reference/SentinelAudit.md) | 16 | registros de auditoria Sentinel para alterações em recursos e operações Sentinel. |
| [SentinelHealth](../reference/SentinelHealth.md) | 17 | Registros de integridade Sentinel para conectores, análises, automação e monitoramento operacional. |
| [ThreatIntelIndicators](../reference/ThreatIntelIndicators.md) | 26 | Indicadores de inteligência de ameaças armazenados em Sentinel para correspondência IOC e buscas orientadas por inteligência. |
| [Watchlist](../reference/Watchlist.md) | 30 | Registros de Watchlist Sentinel para listas de permissões, contexto de negócios, listas IOC e enriquecimento. |

## Perguntas comuns
- Que pergunta de segurança esta tabela pode responder?
- Qual entidade ele pode identificar: usuário, host, IP, URL, hash, recurso de nuvem ou incidente?
- A qual outra tabela deveria ser associada para fins de contexto?
- Qual cadência de caça o utiliza: Diariamente, Semanalmente, Intel ou Mensalmente?
