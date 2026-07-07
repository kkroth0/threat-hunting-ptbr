# Nome da tabela

## Objetivo de caça
Quais questões de segurança esta tabela pode responder?

## Fonte de dados
Qual ferramenta, plataforma ou conector alimenta esta tabela?

## Campos-chave
| Campo | Tipo | Por que é importante |
| --- | --- | --- |

## Junções comuns
- Tabela:
- Campo de adesão:

## Exemplo de caça
- Ideia de caça:

## Inicial KQL
```kql
TableName
| where TimeGenerated >= ago(24h)
| take 100
```
