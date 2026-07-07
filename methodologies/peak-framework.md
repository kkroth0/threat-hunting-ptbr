# Estrutura PEAK

PEAK significa Preparar, Executar e Agir com Conhecimento. É útil porque evita que uma busca se torne apenas uma consulta. Uma busca no estilo PEAK registra por que a busca existe, como seu escopo foi definido, quais evidências foram pesquisadas, o que mudou durante a análise e qual conhecimento deve ser reutilizado.

Este repositório adapta PEAK em um fluxo de trabalho centrado em Sentinel:

```text
Prepare -> Execute -> Act
       Knowledge is captured during every phase
```

## PEAK Fases
| Fase | Finalidade | Ações centradas em Sentinel |
| --- | --- | --- |
| Preparar | Defina a busca antes de tocar nos dados. | Escreva a hipótese ou pergunta, mapeie as tabelas Sentinel necessárias, liste os campos, defina lookback, identifique as entidades esperadas e confirme a cobertura. |
| Executar | Execute a caça e refine-a. | Execute KQL, inspecione linhas brutas, normalize campos, junte contexto, ajuste limites, capture versões de consulta e valide resultados. |
| Agir | Transforme resultados em melhoria de segurança. | Escale incidentes, crie detecções, adicione listas de observação, corrija analisadores, documente falsos positivos, atualize a página de busca e informe as partes interessadas. |
| Conhecimento | Preservar o que foi aprendido. | Registre evidências, suposições, lacunas, decisões, referências e buscas de acompanhamento. |

## Categorias de caça
HEARTH mapeia o conteúdo de caça PEAK em três categorias. Esta biblioteca usa a mesma ideia, mas mantém Microsoft Sentinel como camada de execução.

| Categoria PEAK/HEARTH | Significado | Mapeamento Local |
| --- | --- | --- |
| Chamas | Caçadas baseadas em hipóteses. | [Caça baseada em hipóteses](hypothesis-driven.md) e caças de cenário em `hunts/weekly/` ou `hunts/intel/`. |
| Brasas | Linha de base e exploração. | [Data Driven Hunting](data-driven.md), criação de perfil de tabela e análises recorrentes de Daily/Monthly. |
| Alquimia | Detecção e análise assistida por modelo. | [Model Assisted Hunting](model-assisted.md), pontuação de raridade, agrupamento e caças de séries temporais. |

## ABLE Escopo
Use ABLE para tornar uma busca testável antes de escrever KQL.

| Campo | Pergunta | Exemplo |
| --- | --- | --- |
| Ator | Quem pode realizar esse comportamento? Ator é opcional. | Afiliado de ransomware, usuário interno, usuário comprometido, ator desconhecido. |
| Comportamento | Que ação procuramos? | Spray de senha, PowerShell suspeito, abuso de extensão VM, saída de dados. |
| Localização | Onde apareceriam as evidências? | Entra ID, ponto de extremidade Windows, Cloudflare, Netskope, AzureActivity, Orca, Trend Vision One. |
| Evidência | Quais registros e campos comprovam ou refutam isso? | `SigninLogs.UserPrincipalName`, `Cloudflare_CL.ClientIP_s`, `SecurityEvent.EventID`, `AzureActivity.OperationNameValue`. |

## Preparar lista de verificação
- Defina o tipo de busca: hipótese, dados, informações ou modelo assistido.
- Escreva uma pergunta clara sobre a caça.
- Identifique as tabelas Sentinel necessárias.
- Verifique a integridade e retenção dos dados.
- Liste os principais campos e entidades esperadas.
- Observe incidentes, detecções, tickets ou testes da equipe vermelha relacionados.
- Definir critérios de sucesso: o que confirmaria, refutaria ou refinaria a caçada?

## Executar lista de verificação
- Comece com uma consulta ampla e inspecione exemplos brutos.
- Projetar os campos necessários para revisão do analista.
- Normalize entidades usando [Normalização de campo](../sentinel/tables/field-normalization.md).
- Junte-se ao enriquecimento de `IdentityInfo`, `BehaviorAnalytics`, `Watchlist`, `ThreatIntelIndicators` ou tabelas de fornecedores quando útil.
- Ajuste para falsos positivos esperados.
- Salve KQL refinado na [Biblioteca KQL](../sentinel/kql/README.md).

## Lista de verificação de atos
- Escalar possíveis descobertas maliciosas.
- Criar ou atualizar regras analíticas Sentinel.
- Adicione listas de observação para entidades reconhecidamente boas ou ativos de alto risco.
- Documentar lacunas de dados e problemas de integridade do conector.
- Atualize a página de busca com o que funcionou e o que não funcionou.
- Crie caçadas de acompanhamento quando o resultado expõe uma questão mais ampla.

## Captura de conhecimento
Cada caçada concluída deve deixar para trás:

- Xqzph00000xqz final e retrospectiva.
- Tabelas e campos utilizados.
- Exemplos de verdadeiros positivos, falsos positivos ou evidências de não ocorrência.
- Notas e decisão do analista.
- Detecção de candidato ou motivo para não automatizar.
- Proprietário de acompanhamento e data de vencimento.
- Referências utilizadas.

## Como isso se adapta à biblioteca
- Comece a partir de um cenário em [Hunts](../hunts/README.md).
- Confirme a cobertura em [tabelas Sentinel](../sentinel/tables/index.md).
- Execute ou ajuste a correspondência [KQL](../sentinel/kql/README.md).
- Documente os resultados usando o [modelo de caça](../templates/hunt-template.md).

## Referências
- [Modelo HEARTH PEAK](https://github.com/THORCollective/HEARTH/blob/main/Kindling/PEAK-Template.md)
- [Modelo de caça HEARTH](https://github.com/THORCollective/HEARTH/blob/main/Kindling/Hunt-Template.md)
- [Estrutura de caça a ameaças do Splunk PEAK](https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html)
