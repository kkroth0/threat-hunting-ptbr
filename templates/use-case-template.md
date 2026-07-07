# Use o título do caso

## Metadados
| Campo | Valor |
| --- | --- |
| Caso de uso ID | `UC-000` |
| Estado | Rascunho, Teste, Produção, Ajuste, Aposentado |
| Proprietário |  |
| Criado | YYYY-MM-DD |
| Última revisão | YYYY-MM-DD |
| Caça à fonte | Link para a página de caça |
| Fonte KQL | Link para o arquivo KQL |
| Gravidade | Crítico, Alto, Médio, Baixo, Informativo |
| Confiança | Alto, Médio, Baixo |
| Cadência | Programado, quase em tempo real, revisão diária, revisão semanal |

## Objetivo
Que comportamento este caso de uso deve detectar?

## Hipótese de Detecção
```text
If this behavior happens, it may indicate...
```

## Escopo
| Item Escopo | Valor |
| --- | --- |
| Ambientes incluídos |  |
| Ambientes excluídos |  |
| Usuários ou grupos |  |
| Hosts ou ativos |  |
| Países ou regiões |  |
| Unidades de negócios |  |

## MITRE ATT&CK Mapeamento
| Tática | Técnica | Notas |
| --- | --- | --- |
|  |  |  |

## Requisitos de dados
| Ferramenta | Tabela Sentinel | Campos obrigatórios | Notas |
| --- | --- | --- | --- |
|  |  |  |  |

## Mapeamento de entidade
| Entidade | Campos |
| --- | --- |
| Conta |  |
| Anfitrião |  |
| IP |  |
| URL ou domínio |  |
| Hash de arquivo |  |
| Recurso de nuvem |  |

## Lógica de Detecção
```kql
let lookback = 1d;
TableName
| where TimeGenerated >= ago(lookback)
```

## Configurações de regras Sentinel
| Configuração | Valor |
| --- | --- |
| Frequência de consulta |  |
| Período de consulta |  |
| Limiar de disparo |  |
| Agrupamento de eventos |  |
| Agrupamento de incidentes |  |
| Supressão |  |
| Táticas |  |
| Técnicas |  |

## Falsos Positivos
| Cenário | Abordagem de ajuste |
| --- | --- |
|  |  |

## Listas de observação
- Lista de observação necessária:
- Lista de observação opcional:

## Plano de teste
| Teste | Resultado | Notas |
| --- | --- | --- |
| Repetição histórica |  |  |
| Revisão benigna conhecida |  |  |
| Simulação verdadeiro-positiva |  |  |
| Verificação de mapeamento de entidade |  |  |
| revisão de SOC |  |  |

## Etapas de triagem
1. Revise as entidades de alerta.
2. Valide a atividade na tabela de origem.
3. Verifique logins, eventos de endpoint, atividades de rede e incidentes relacionados.
4. Confirme se a entidade é esperada ou aprovada.
5. Escale, feche como benigno ou crie uma tarefa de ajuste.

## Orientação de resposta
| Condição | Ação |
| --- | --- |
| Malicioso confirmado | Escalar para resposta a incidentes. |
| Suspeito, mas não confirmado | Designe o proprietário da investigação e colete evidências. |
| Atividade benigna esperada | Documente e ajuste se houver ruído. |
| Problema de qualidade dos dados | Abra o analisador, o conector ou a tarefa de criação de log. |

## Métricas
- Alertas por semana:
- Verdadeiros positivos:
- Falsos positivos:
- Principal motivo de falso positivo:
- Tempo médio para triagem:
- Última alteração de afinação:

## Histórico de alterações
| Data | Alterar | Proprietário |
| --- | --- | --- |
|  |  |  |
