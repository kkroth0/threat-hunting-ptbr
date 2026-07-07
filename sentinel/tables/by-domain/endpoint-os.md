# Endpoint e sistemas operacionais

Windows, Linux, integridade do agente, processo, logon, serviço, script e telemetria do host.

## Tabelas
| Tabela | Campos | Objetivo de caça |
| --- | ---: | --- |
| [SecurityEvent](../reference/SecurityEvent.md) | 228 | Windows Logs de eventos de segurança coletados em Sentinel, úteis para buscas de logon, processo, conta, serviço e política. |
| [WindowsEvent](../reference/WindowsEvent.md) | 26 | Windows Logs de eventos coletados com AMA, úteis para endpoint específico do provedor e buscas PowerShell. |
| [Syslog](../reference/Syslog.md) | 17 | Tabela Sentinel/Log Analytics disponível para busca e correlação. |
| [Heartbeat](../reference/Heartbeat.md) | 31 | Registros de Heartbeat do agente usados ​​para verificar a cobertura e a integridade da coleta. |
| [AMAAgentHealth_CL](../reference/AMAAgentHealth_CL.md) | 8 | Tabela Sentinel/Log Analytics disponível para busca e correlação. |
| [TrendMicro_XDR_OAT_CL](../reference/TrendMicro_XDR_OAT_CL.md) | 387 | Tabela customizada Trend Vision One usada para integridade, detecção ou busca no ambiente de trabalho endpoint/XDR. |
| [TrendMicro_XDR_WORKBENCH_CL](../reference/TrendMicro_XDR_WORKBENCH_CL.md) | 44 | Tabela customizada Trend Vision One usada para integridade, detecção ou busca no ambiente de trabalho endpoint/XDR. |
| [TrendMicro_XDR_Health_Check_CL](../reference/TrendMicro_XDR_Health_Check_CL.md) | 13 | Tabela customizada Trend Vision One usada para integridade, detecção ou busca no ambiente de trabalho endpoint/XDR. |
| [TrendMicro_XDR_OAT_Health_Check_CL](../reference/TrendMicro_XDR_OAT_Health_Check_CL.md) | 12 | Tabela customizada Trend Vision One usada para integridade, detecção ou busca no ambiente de trabalho endpoint/XDR. |

## Perguntas comuns
- Que pergunta de segurança esta tabela pode responder?
- Qual entidade ele pode identificar: usuário, host, IP, URL, hash, recurso de nuvem ou incidente?
- A qual outra tabela deveria ser associada para fins de contexto?
- Qual cadência de caça o utiliza: Diariamente, Semanalmente, Intel ou Mensalmente?
