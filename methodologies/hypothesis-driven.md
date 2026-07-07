# Caça baseada em hipóteses

Use a caça orientada por hipóteses quando puder expressar uma declaração específica e testável sobre o comportamento, uso indevido ou abuso do adversário.

Boa hipótese:

```text
An attacker with valid credentials is accessing privileged cloud resources from a new location and then changing role assignments.
```

Hipótese fraca:

```text
Find bad logins.
```

A diferença é o escopo. Uma hipótese forte fornece critérios de comportamento, localização, evidências e validação.

## Quando usar
- Um relatório de ameaças descreve um comportamento relevante para o seu ambiente.
- Um incidente anterior sugere um caminho de abuso repetível.
- Existe uma lacuna de detecção para uma técnica MITRE ATT&CK conhecida.
- Um red team ou um teste de penetração usou uma técnica que você deseja pesquisar historicamente.
- Um alerta de ferramenta é muito restrito e você deseja monitorar o comportamento ao redor.

## Entradas
| Entrada | Por que é importante |
| --- | --- |
| Hipótese | Define o que você está tentando provar, refutar ou refinar. |
| MITRE tactic/technique | Ajuda a mapear o comportamento de acordo com a estratégia do adversário conhecido. |
| Tabelas obrigatórias | Impede a caça contra telemetria ausente ou fraca. |
| Campos-chave | Torna a consulta testável e revisável. |
| Atividade benigna esperada | Ajuda a ajustar falsos positivos. |
| Fonte de validação | Confirma que um resultado suspeito é real. |

## ABLE Escopo
| ABLE Campo | Sentinel Exemplo |
| --- | --- |
| Ator | Atacante desconhecido, usuário comprometido, operador de ransomware, insider, diretor de serviço. |
| Comportamento | Spray de senha, PowerShell suspeito, atribuição de função de nuvem, tentativa de desvio de WAF, exfiltração de DLP. |
| Localização | `SigninLogs`, `AuditLogs`, `SecurityEvent`, `AzureActivity`, `Cloudflare_CL`, `NetskopeAlerts_CL`, `TrendMicro_XDR_OAT_CL`. |
| Evidência | IDs de eventos, nomes de operações, usuário, IP, host, URL, linha de comando do processo, hash de arquivo, nível de risco, alerta ID. |

## Padrão de execução Sentinel
1. Escreva a hipótese na página de busca.
2. Confirme se as tabelas necessárias contêm dados do período de lookback.
3. Comece com uma pesquisa ampla KQL para o comportamento principal.
4. Inspecione as linhas brutas antes de resumir.
5. Adicione normalização e enriquecimento de entidade.
6. Adicione junções somente depois que o comportamento base estiver visível.
7. Ajuste falsos positivos com listas de observação, usuários bons, hosts administradores conhecidos, aplicativos esperados e janelas de manutenção.
8. Valide resultados suspeitos com outra tabela ou ferramenta.

## Exemplos de padrões de hipóteses
| Cenário | Tabelas |
| --- | --- |
| Spray de senha seguido de login bem-sucedido. | `SigninLogs`, `IdentityInfo`, `BehaviorAnalytics`. |
| Execução suspeita de PowerShell em endpoints. | `SecurityEvent`, `WindowsEvent`, `TrendMicro_XDR_OAT_CL`. |
| Azure VM Executar abuso de comando. | `AzureActivity`, `SecurityAlert`, telemetria de terminal, se disponível. |
| Ataque WAF seguido por resposta de origem bem-sucedida. | `Cloudflare_CL`, logs de aplicativos, `SecurityAlert`. |
| Recuperação de credenciais privilegiadas fora do fluxo de trabalho normal. | `CyberArk_AuditEvents_CL`, `SigninLogs`, `AuditLogs`. |

## Tipos de resultados
| Resultado | Significado | Próximo passo |
| --- | --- | --- |
| Malicioso confirmado | As evidências apoiam o compromisso ou o abuso ativo. | Escalar para resposta a incidentes. |
| Suspeito, mas não confirmado | As evidências requerem mais contexto. | Enriquecer e atribuir acompanhamento. |
| Padrão benigno | O comportamento existe, mas é esperado. | Adicione notas falso-positivas ou lista de observação. |
| Nenhuma evidência encontrada | Hipótese não observada nos dados atuais. | Registre lookback e limites de cobertura. |
| Lacuna de dados | A telemetria necessária está ausente ou fraca. | Crie tarefa de conector, analisador, retenção ou registro em log. |

## Ajuste de cadência
- Diariamente: hipóteses estreitas de abuso ativo.
- Semanalmente: comportamento que necessita de uma linha de base de 7 a 30 dias.
- Intel: TTPs de novos relatórios.
- Mensalmente: lacunas estratégicas em técnicas de alto valor.

## Como isso se adapta à biblioteca
- Comece a partir de um cenário em [Hunts](../hunts/README.md).
- Confirme a cobertura em [tabelas Sentinel](../sentinel/tables/index.md).
- Execute ou ajuste a correspondência [KQL](../sentinel/kql/README.md).
- Documente os resultados usando o [modelo de caça](../templates/hunt-template.md).

## Referências
- [HEARTH Chamas](https://github.com/THORCollective/HEARTH/tree/main/Flames)
- [Modelo de caça HEARTH](https://github.com/THORCollective/HEARTH/blob/main/Kindling/Hunt-Template.md)
- [MITRE ATT&CK](https://attack.mitre.org/)
