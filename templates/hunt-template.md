# Título de caça

## Metadados
| Campo | Valor |
| --- | --- |
| Caça ID | `HUNT-000` |
| Metodologia | Hipótese, Dados, Intel, Modelo Assistido |
| Cadência | Diariamente, Semanalmente, Intel, Mensalmente ou ad hoc |
| Estado | Rascunho, Ativo, Completo, Aposentado |
| Analista | Nome |
| Data de início | YYYY-MM-DD |
| Data de conclusão | YYYY-MM-DD |
| Solicitante | SOC, IR, TI, Engenharia de detecção, Red Team, Business ou autodirigido |
| Gravidade | Crítico, Alto, Médio, Baixo, Informativo |

## Objetivo
Que pergunta de segurança esta caçada está tentando responder?

## Hipótese ou Pergunta
Escreva uma declaração clara e testável.

```text
An attacker may be...
```

Para buscas baseadas em dados, escreva uma pergunta exploratória:

```text
What does normal activity look like for...
```

## PEAK Fase: Preparação

### ABLE Escopo
| Campo | Descrição |
| --- | --- |
| Ator | Ator de ameaça, persona, tipo de usuário ou N/A. |
| Comportamento | A ação, técnica, caminho do abuso, anomalia ou sequência. |
| Localização | Plataforma, ferramenta, ambiente ou tabela Sentinel onde as evidências devem aparecer. |
| Evidência | Logs, campos, exemplos e fontes de validação necessários. |

## Tabelas Sentinel
-`TableName`
-`TableName`

## Ferramentas
- Ferramenta:
- Ferramenta:

## Campos-chave
| Entidade | Campos |
| --- | --- |
| Usuário |  |
| Anfitrião |  |
| IP |  |
| URL ou domínio |  |
| Arquivo ou hash |  |
| Recurso de nuvem |  |

## Referências
- Ligação:
- Bilhete interno:
- Detecção relacionada:

## PEAK Fase: Executar

### Inicial KQL
```kql
let lookback = 7d;
TableName
| where TimeGenerated >= ago(lookback)
| take 100
```

### Notas de consulta
- Contagem de resultados:
- Campos faltando:
- Falsos positivos:
- Refinamento necessário:

### Refinado KQL
```kql
// Save final query here or link to sentinel/kql/<cadence>/<query>.kql
```

### Validação
| Resultado | Fonte de validação | Decisão |
| --- | --- | --- |
|  |  | Benigno, Suspeito, Incidente, Lacuna de Dados, Candidato a Detecção |

## PEAK Fase: Agir

## Descobertas
| Encontrando | Evidência | Ingresso ou Link | Proprietário |
| --- | --- | --- | --- |
|  |  |  |  |

## Oportunidade de detecção
| Pergunta | Resposta |
| --- | --- |
| Isso deveria se tornar uma regra analítica Sentinel? |  |
| É necessária uma lista de observação ou lista de permissões? |  |
| Precisa de trabalho de analisador ou normalização de campo? |  |
| Deveria se tornar uma pasta de trabalho ou painel? |  |
| Deve ser adicionado ao calendário de caça? |  |

## Captura de conhecimento
- O que aprendemos?
- O que funcionou?
- O que falhou?
- O que deve mudar antes da próxima corrida?
- Que caçadas de acompanhamento foram criadas?
- Quais equipes precisam do resultado?

## Resultado Final
Escolha um ou mais:

- Incidente escalado.
- Detecção criada ou atualizada.
- Watchlist criada ou atualizada.
- Problema no analisador ou conector aberto.
- Orientação falso-positiva documentada.
- Nenhuma evidência encontrada com os dados atuais.
- Caça de acompanhamento criada.
