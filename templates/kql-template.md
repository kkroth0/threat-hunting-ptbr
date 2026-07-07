# Nome da consulta

## Objetivo
O que esta consulta encontra?

## Metodologia
Hipótese, Dados, Intel ou Modelo Assistido.

## Cadência
Diariamente, Semanalmente, Intel, Mensalmente ou ad hoc.

## Tabelas
- Tabela:

## Entidades
- Usuário:
- Anfitrião:
- Fonte IP:
- Destino IP:
-URL/domain:
-File/hash:
- Recurso de nuvem:

## Consulta
```kql
let lookback = 1d;
TableName
| where TimeGenerated >= ago(lookback)
```

## Notas de ajuste
- Limites:
- Falsos positivos conhecidos:
- Listas de observação obrigatórias:

## Notas de validação
- Confirmado com:
- Resultado esperado:
- Critérios de escalonamento:
