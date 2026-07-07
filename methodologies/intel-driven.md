# Caça orientada por Intel

Use a busca orientada por inteligência quando novas informações precisarem ser testadas em seu ambiente. A inteligência pode ser externa ou interna, tática ou estratégica, baseada em indicadores ou baseada em comportamento.

A caça conduzida pela Intel pergunta:

```text
Did this threat, behavior, infrastructure, exploit, or campaign affect us?
```

## Tipos de inteligência
| Tipo | O que ele oferece | Risco de caça |
| --- | --- | --- |
| IOC | IPs, domínios, URLs, hashes, endereços de e-mail. | Rápido para pesquisar, variantes fáceis de perder. |
| TTP | Comportamento, uso de ferramentas, sequência, técnica. | Mais durável, requer melhor mapeamento de dados. |
| CVE ou explorar | Vulnerabilidade, software alvo, caminho de exploração. | Requer contexto de ativo e exposição. |
| Relatório de campanha | Ator, malware, infraestrutura, técnicas. | Pode incluir IOCs e comportamentos amplos. |
| Incidente interno | Atividade real do seu ambiente. | Alta relevância e forte valor de acompanhamento. |
| Alerta de fornecedor | Detecção ou análise específica da ferramenta. | Precisa de validação fora da tabela de fornecedores. |

## Triagem Intel
Antes de escrever KQL, responda:

- A fonte é credível e recente?
- A tecnologia afetada está presente no ambiente?
- A inteligência é IOC, comportamento, vulnerabilidade ou todos os três?
- Quais tabelas Sentinel podem comprovar exposição ou atividade?
- Qual retrospectiva é apropriada?
- O que tornaria um acerto acionável?

## Padrão de execução Sentinel
1. Normalize IOCs em `ThreatIntelIndicators` ou em uma lista de observação Sentinel.
2. Converta TTPs em comportamentos e campos obrigatórios.
3. Mapeie o comportamento para tabelas em [catálogo de tabelas Sentinel](../sentinel/tables/index.md).
4. Execute primeiro varreduras amplas e depois junções direcionadas.
5. Transforme os acessos em usuários, hosts, IPs, URLs, hashes, recursos de nuvem, alertas e incidentes.
6. Valide com pelo menos uma fonte independente, quando possível.
7. Documente o resultado, mesmo quando nenhuma evidência for encontrada.

## IOC Padrão de caça
Tabelas úteis para varreduras IOC:

-`ThreatIntelIndicators`
-`CommonSecurityLog`
-`Cloudflare_CL`
-`NetskopeAlerts_CL`
-`NetskopeEventsApplication_CL`
-`NetskopeEventsNetwork_CL`
-`TrendMicro_XDR_OAT_CL`
-`TrendMicro_XDR_WORKBENCH_CL`
-`OrcaAlerts_CL`

Consulta inicial:

- [`ioc-ip-domain-url-hash-sweep.kql`](../sentinel/kql/intel/ioc-ip-domain-url-hash-sweep.kql)

## TTP Padrão de caça
A caça TTP é mais durável do que a caça IOC pura. Converta o relatório em:

| TTP Detalhe | Exemplo |
| --- | --- |
| Técnica | Contas válidas, execução de comandos, comando de administração de nuvem, exfiltração. |
| Dados necessários | Entradas de identidade, logs de plano de controle Azure, logs de processos de endpoint, logs de proxy. |
| Caminho da entidade | Usuário -> IP -> aplicativo -> recurso de nuvem -> processo -> alerta. |
| Sequência esperada | Logins com falha -> sucesso -> alteração de administrador -> saída incomum. |
| Validação | Tabela independente, console de ferramentas, confirmação do proprietário ou evidência de incidente. |

## Saída
Uma busca conduzida por inteligência deve produzir:

- Fonte e data da Intel revisadas.
- IOCs ou comportamentos testados.
- Tabelas pesquisadas e lookback.
- Acertos e falsos positivos validados.
- Lacunas de cobertura.
- Detecções recomendadas, listas de observação ou caçadas de acompanhamento.

## Ajuste de cadência
- Execute imediatamente para exploração ativa ou IOCs de alta confiança.
- Execute dentro de 24 horas para obter indicadores de campanha confiáveis.
- Adicione caçadas TTP mais amplas à cadência semanal.
- Revise mensalmente informações estratégicas e lacunas de cobertura.

## Como isso se adapta à biblioteca
- Comece a partir de um cenário em [Hunts](../hunts/README.md).
- Confirme a cobertura em [tabelas Sentinel](../sentinel/tables/index.md).
- Execute ou ajuste a correspondência [KQL](../sentinel/kql/README.md).
- Documente os resultados usando o [modelo de caça](../templates/hunt-template.md).

## Referências
- [Recursos HEARTH](https://github.com/THORCollective/HEARTH/blob/main/Kindling/Resources.md)
- [HEARTH Chamas](https://github.com/THORCollective/HEARTH/tree/main/Flames)
- [MITRE ATT&CK](https://attack.mitre.org/)
