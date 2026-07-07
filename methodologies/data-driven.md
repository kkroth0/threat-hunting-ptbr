# Caça baseada em dados

Use a caça orientada por dados quando a caça começar a partir da telemetria, em vez de uma hipótese de adversário totalmente formada. Este método é especialmente útil ao integrar uma nova tabela, aprender uma nova ferramenta, construir linhas de base ou procurar valores discrepantes.

A caça orientada por dados pergunta:

```text
What does normal look like here, and what is unusual enough to investigate?
```

## Quando usar
- Um novo conector ou tabela personalizada foi adicionado a Sentinel.
- Você precisa entender campos, valores, volume e cobertura.
- Os alertas são barulhentos e você precisa de linhas de base melhores.
- Você deseja encontrar usuários, hosts, IPs, URLs, aplicativos, processos ou recursos de nuvem incomuns.
- Você está preparando hipóteses futuras ou caçadas assistidas por modelo.

## Perguntas básicas
| Pergunta | Exemplo KQL Direção |
| --- | --- |
| Quais entidades são mais ativas? | Resuma por usuário, host, IP, URL, aplicativo ou recurso. |
| Quais valores são raros? | Compare os últimos 7 dias com os 30 dias anteriores. |
| Quais campos estão faltando? | Contar campos-chave nulos ou vazios. |
| O que mudou recentemente? | Compare a janela atual com a linha de base histórica. |
| Quais tabelas pararam de enviar? | Revise `Heartbeat`, `SentinelHealth`, `Usage` e tabelas de integridade do conector customizado. |

## Padrão de perfil de dados Sentinel
```kql
let lookback = 7d;
TableName
| where TimeGenerated >= ago(lookback)
| summarize
    Events = count(),
    FirstSeen = min(TimeGenerated),
    LastSeen = max(TimeGenerated),
    ExampleValues = make_set(tostring(FieldName), 20)
    by bin(TimeGenerated, 1d)
| order by TimeGenerated desc
```

## Tabelas Sentinel úteis
| Domínio de Dados | Tabelas |
| --- | --- |
| Identidade | `SigninLogs`, `AuditLogs`, `IdentityInfo`, `BehaviorAnalytics`, `UserPeerAnalytics`. |
| Ponto final | `SecurityEvent`, `WindowsEvent`, `Syslog`, `TrendMicro_XDR_OAT_CL`. |
| Rede e Borda | `CommonSecurityLog`, `Cloudflare_CL`, `NetskopeEventsNetwork_CL`, `NetskopeEventsConnection_CL`, `NetskopeEventsPage_CL`. |
| SaaS e DLP | `OfficeActivity`, `NetskopeEventsApplication_CL`, `NetskopeAlerts_CL`. |
| Nuvem e Postura | `AzureActivity`, `AzureDiagnostics`, `OrcaAlerts_CL`. |
| Sentinel Operações | `SecurityIncident`, `SecurityAlert`, `SentinelHealth`, `Usage`, `LAQueryLogs`. |

## Tipos de linha de base
| Linha de base | Descrição | Exemplo |
| --- | --- | --- |
| Volume | Conte eventos por hora, entidade ou tabela. | Falhas de login por usuário por dia. |
| Raridade | Encontre valores nunca vistos antes ou raramente vistos. | Novo agente de usuário para um usuário. |
| Par | Compare o comportamento da entidade com entidades semelhantes. | O usuário baixa muito mais do que seus pares. |
| Sazonalidade | Compare o comportamento por hora, dia ou ciclo de negócios. | Atividade administrativa fora da janela normal de manutenção. |
| Cobertura | Confirme se os logs estão presentes e utilizáveis. | O conector parou de enviar eventos. |

## Saída
Uma busca orientada por dados deve produzir:

- Uma consulta de base.
- Padrões normais conhecidos.
- Exemplos atípicos.
- Campos úteis ou não confiáveis.
- Novas ideias de hipóteses.
- Notas de qualidade e retenção de dados.
- Listas de observação ou listas de permissões de candidatos.

## Ajuste de cadência
- Diariamente: integridade do conector, valores discrepantes de alto risco, volume de alertas.
- Semanalmente: acesso raro, saída superior, novos aplicativos, nova atividade administrativa.
- Mensalmente: revisão de ingestão, revisão de custos, cobertura de detecção, qualidade da tabela.

## Como isso se adapta à biblioteca
- Comece a partir de um cenário em [Hunts](../hunts/README.md).
- Confirme a cobertura em [tabelas Sentinel](../sentinel/tables/index.md).
- Execute ou ajuste a correspondência [KQL](../sentinel/kql/README.md).
- Documente os resultados usando o [modelo de caça](../templates/hunt-template.md).

## Referências
- [HEARTH Brasas](https://github.com/THORCollective/HEARTH/tree/main/Embers)
- [Recursos HEARTH](https://github.com/THORCollective/HEARTH/blob/main/Kindling/Resources.md)
- [Caça de linha de base do Splunk com PEAK](https://www.splunk.com/en_us/blog/security/peak-baseline-hunting.html)
