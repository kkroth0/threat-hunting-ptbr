# Caça Assistida por Modelo

Use a caça assistida por modelo quando regras estáticas ou limites simples não forem suficientes. Este método usa pontuação, raridade, agrupamento, análise de série temporal ou aprendizado de máquina para revelar comportamentos que merecem revisão do analista.

A caça assistida por modelo pergunta:

```text
Can a model or statistical method find suspicious behavior that a fixed query would miss?
```

## Quando usar
- O comportamento é sutil, variável ou específico do ambiente.
- Você precisa encontrar combinações raras em vez de valores ruins conhecidos.
- O conjunto de dados é grande o suficiente para estabelecer uma linha de base.
- Você precisa classificar o risco em vez de retornar uma correspondência binária.
- Um ser humano pode validar os melhores resultados.

## Métodos Comuns
| Método | Usar para | Exemplo compatível com Sentinel |
| --- | --- | --- |
| Pontuação de raridade | Valores novos ou incomuns. | Novo país, aplicativo, agente do usuário, destino, pai do processo. |
| Desvio da série temporal | Picos ou quedas ao longo do tempo. | Volume de saída, logins com falha, blocos WAF, volume de alerta. |
| Comparação entre pares | Valores discrepantes em comparação com usuários ou hosts semelhantes. | O usuário baixa muito mais do que seus pares. |
| Agrupamento | Agrupe comportamentos semelhantes e inspecione clusters pequenos ou estranhos. | Processar linhas de comando, agentes de usuário, padrões DNS. |
| Análise de sequência | Ordenação suspeita de eventos. | Falhas -> sucesso -> mudança de privilégio -> ação na nuvem. |
| Pontuação de recursos | Modelo de risco ponderado. | Novo IP mais aplicativo arriscado mais dispositivo não gerenciado mais MFA com falha. |

## Requisitos de dados
Antes de usar uma abordagem assistida por modelo, confirme:

- A tabela possui dados históricos suficientes.
- Os campos-chave são preenchidos de forma consistente.
- As entidades estão normalizadas.
- O bom comportamento administrativo é documentado.
- O resultado pode ser explicado a um analista.
- Existe um caminho de revisão para falsos positivos.

## Padrão de execução Sentinel
1. Primeiro crie o perfil da tabela com busca orientada por dados.
2. Defina a entidade que está sendo modelada: usuário, host, IP, URL, aplicativo, processo, recurso.
3. Escolha características que representem comportamento.
4. Crie uma pontuação ou linha de base KQL simples antes de passar para ferramentas mais pesadas.
5. Revise manualmente os resultados mais bem classificados.
6. Rotule falsos positivos e padrões conhecidos como bons.
7. Converta recursos estáveis em detecções, listas de observação ou painéis.

## KQL-Exemplo de primeira pontuação
```kql
let lookback = 7d;
SigninLogs
| where TimeGenerated >= ago(lookback)
| summarize
    Apps = dcount(AppDisplayName),
    IPs = dcount(IPAddress),
    Countries = dcount(tostring(LocationDetails.countryOrRegion)),
    Failures = countif(ResultType != "0"),
    Successes = countif(ResultType == "0")
    by UserPrincipalName
| extend RiskScore =
    (Apps * 2)
    + (IPs * 2)
    + (Countries * 3)
    + (Failures * 1)
    + iff(Successes > 0 and Failures > 10, 10, 0)
| order by RiskScore desc
```

## Bons candidatos assistidos por modelo
| Cenário | Tabelas |
| --- | --- |
| Padrão de acesso de identidade raro. | `SigninLogs`, `IdentityInfo`, `BehaviorAnalytics`. |
| Volume de tráfego de saída anormal. | `CommonSecurityLog`, `NetskopeEventsNetwork_CL`, `Cloudflare_CL`. |
| Cadeia de processos de endpoint rara. | `SecurityEvent`, `WindowsEvent`, `TrendMicro_XDR_OAT_CL`. |
| Ação incomum de recursos em nuvem. | `AzureActivity`, `AzureDiagnostics`, `OrcaAlerts_CL`. |
| outlier de atividade DLP ou SaaS. | `NetskopeAlerts_CL`, `NetskopeEventsApplication_CL`, `OfficeActivity`. |

## Armadilhas
- Os modelos podem ocultar a fraca qualidade dos dados. Crie o perfil dos dados primeiro.
- Uma pontuação alta de anomalia não é prova de comprometimento.
- Comportamentos comerciais raros podem parecer maliciosos.
- Os limites variam à medida que o ambiente muda.
- Se o método não puder ser explicado, é difícil operacionalizá-lo.

## Saída
Uma caça assistida por modelo deve produzir:

- Recursos usados.
- Período de referência.
- Pontuação ou lógica do modelo.
- Principais resultados revisados.
- Notas falso-positivas.
- Recomendação: detecção, painel, notebook, lista de observação ou nenhuma ação.

## Como isso se adapta à biblioteca
- Use [Data Driven Hunting](data-driven.md) para entender a tabela primeiro.
- Salve a lógica repetível na [Biblioteca KQL](../sentinel/kql/README.md).
- Documente os resultados usando o [modelo de caça](../templates/hunt-template.md).

## Referências
- [HEARTH Alquimia](https://github.com/THORCollective/HEARTH/tree/main/Alchemy)
- [Caça a ameaças assistida por modelo Splunk com PEAK](https://www.splunk.com/en_us/blog/security/peak-framework-math-model-assisted-threat-hunting.html)
- [Estrutura de caça a ameaças do Splunk PEAK](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html)
