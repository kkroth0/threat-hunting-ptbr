# Visão geral da caça a ameaças

A caça a ameaças é uma investigação estruturada para comportamentos suspeitos que podem ainda não estar cobertos por alertas. Neste repositório, a caça começa com uma pergunta, mapeia essa pergunta para dados Sentinel, executa KQL, valida os resultados e preserva o conhecimento para que a próxima caça seja mais fácil.

Esta biblioteca é construída em torno de um modelo operacional:

```text
Question -> Data coverage -> Query -> Validation -> Finding -> Detection or knowledge
```

## Resultados da caça
Uma boa caçada não precisa encontrar um incidente para ter sucesso. Deve produzir um ou mais resultados úteis:

- Atividade suspeita ou maliciosa confirmada.
- Uma hipótese fechada com evidências de que o comportamento não foi observado.
- Uma lacuna de dados, problema de analisador, problema de conector ou lacuna de retenção.
- Um padrão falso positivo que deve se tornar uma lista de observação ou regra de ajuste.
- Um candidato a engenharia de detecção.
- Uma nova ideia de caça ou uma versão mais forte da hipótese original.
- Uma melhor compreensão do comportamento normal no ambiente.

## Tipos de caça
| Tipo | Pergunta principal | Use nesta biblioteca |
| --- | --- | --- |
| Hipótese conduzida | Poderia esse comportamento específico do adversário existir aqui? | Use [Hypothesis Driven Hunting](hypothesis-driven.md) e páginas de cenário em `hunts/`. |
| Orientado por dados | O que esses dados mostram e o que é incomum? | Use [Data Driven Hunting](data-driven.md), catálogos de tabelas e linhas de base. |
| Orientado pela Intel | Esta campanha ou relatório IOC, TTP, CVE nos tocou? | Use [Intel Driven Hunting](intel-driven.md) e `sentinel/kql/intel/`. |
| Modelo assistido | Será que a pontuação, a raridade, o agrupamento ou a análise de séries temporais podem revelar o comportamento que os humanos não perceberiam? | Use [Caça assistida por modelo](model-assisted.md). |

## Cadência Operacional
| Cadência | Finalidade | Método de ajuste |
| --- | --- | --- |
| Caça Diária | Capture riscos ativos e verifique a integridade da coleção. | Baseado em dados, baseado em hipóteses, verificações leves de informações. |
| Caça Semanal | Analise mais detalhadamente as linhas de base de identidade, endpoint, rede, SaaS e nuvem. | Baseado em hipóteses e baseado em dados. |
| Caça à Intel | Reaja à inteligência externa ou interna. | Orientado pela inteligência, às vezes por hipóteses. |
| Caça Mensal | Melhore a cobertura, o custo, as detecções e o próprio programa. | Orientado por dados e assistido por modelo. |

Consulte [Hunt Calendar](../cadence/hunt-calendar.md) para ver a programação recorrente.

## Fluxo de trabalho padrão
1. Selecione uma ideia de busca a partir de cadência, fonte de inteligência, incidente anterior, lacuna de detecção ou padrão de dados incomum.
2. Escolha a metodologia que se adapta à questão.
3. Defina o escopo da caça com ator, comportamento, localização e evidências.
4. Confirme se as tabelas Sentinel estão recebendo dados úteis.
5. Execute a primeira consulta KQL e inspecione os exemplos brutos antes de resumir.
6. Refine a consulta com normalização de entidade, listas de permissões, junções e limites.
7. Valide resultados suspeitos com evidências independentes.
8. Registrar descobertas, falsos positivos, lacunas de dados e trabalho de acompanhamento.
9. Decida se a saída se tornará um incidente, uma detecção, uma pasta de trabalho, uma lista de observação, uma correção do analisador ou um item de lista de pendências.

## Padrão de evidência
Cada página de busca deve facilitar a reprodução das evidências:

- Fonte de dados e tabela Sentinel.
- Intervalo de tempo.
- Campos-chave.
- consulta KQL ou arquivo de consulta.
- Entidades encontradas: usuário, host, IP, URL, hash de arquivo, recurso de nuvem, alerta, incidente.
- Fonte de validação.
- Decisão do analista.
- Proprietário de acompanhamento.

## Portões de qualidade
Antes de considerar uma caçada concluída, responda:

- Os dados estavam presentes na retrospectiva completa?
- Os campos críticos foram preenchidos?
- Os falsos positivos foram revisados?
- Os resultados suspeitos foram validados com outra tabela ou ferramenta?
- O resultado foi documentado?
- A busca criou uma tarefa de detecção, ajuste, lista de observação, analisador ou acompanhamento?

## Como isso se adapta à biblioteca
- Comece a partir de um cenário em [Hunts](../hunts/README.md).
- Confirme a cobertura em [tabelas Sentinel](../sentinel/tables/index.md).
- Execute ou ajuste a correspondência [KQL](../sentinel/kql/README.md).
- Documente os resultados usando o [modelo de caça](../templates/hunt-template.md).

## Referências
- [HEARTH](https://github.com/THORCollective/HEARTH)
- [Modelo de caça HEARTH](https://github.com/THORCollective/HEARTH/blob/main/Kindling/Hunt-Template.md)
- [Estrutura de caça a ameaças do Splunk PEAK](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html)
