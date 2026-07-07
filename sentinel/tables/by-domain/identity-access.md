# Identidade e Acesso

Autenticação, atividade de auditoria Entra ID, UEBA, análise de pares, acesso privilegiado e atividade do usuário M365.

## Tabelas
| Tabela | Campos | Objetivo de caça |
| --- | ---: | --- |
| [SigninLogs](../reference/SigninLogs.md) | 95 | Telemetria de login Microsoft Entra ID para autenticação, acesso condicional, risco, dispositivo, IP e buscas de acesso a aplicativos. |
| [AuditLogs](../reference/AuditLogs.md) | 31 | atividade de auditoria Microsoft Entra ID para alterações de diretório, função, aplicativo, política e administrativas. |
| [IdentityInfo](../reference/IdentityInfo.md) | 57 | enriquecimento de identidade UEBA que ajuda a unir detalhes da conta, tags, funções e contexto de identidade para buscar resultados. |
| [BehaviorAnalytics](../reference/BehaviorAnalytics.md) | 33 | Saída de comportamento UEBA usada para risco de entidade, anomalia e investigação baseada em pares. |
| [UserPeerAnalytics](../reference/UserPeerAnalytics.md) | 16 | Análise de grupos de pares de usuários para análise de anomalias de identidade e valores discrepantes. |
| [OfficeActivity](../reference/OfficeActivity.md) | 144 | atividade de auditoria Microsoft 365 para Exchange, SharePoint, Teams e outras cargas de trabalho. |
| [CyberArk_AuditEvents_CL](../reference/CyberArk_AuditEvents_CL.md) | 36 | Eventos de auditoria CyberArk para acesso privilegiado, buscas seguras, de conta e de atividades de sessão. |

## Perguntas comuns
- Que pergunta de segurança esta tabela pode responder?
- Qual entidade ele pode identificar: usuário, host, IP, URL, hash, recurso de nuvem ou incidente?
- A qual outra tabela deveria ser associada para fins de contexto?
- Qual cadência de caça o utiliza: Diariamente, Semanalmente, Intel ou Mensalmente?
