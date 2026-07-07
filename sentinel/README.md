# Microsoft Sentinel

Sentinel é a camada central de dados e busca desta biblioteca.

O fluxo esperado é:

```text
Tool or platform -> Sentinel table -> normalized entities -> hunt scenario -> KQL -> finding or detection
```

## Seções principais
- [Catálogo de tabelas](tables/index.md)
- [Mapa da tabela de ferramentas](tables/tool-table-map.md)
- [Normalização de campo](tables/field-normalization.md)
- [Biblioteca KQL](kql/README.md)

## Catálogo Atual
- Total de tabelas exclusivas com esquema: 45
- Tabelas de conectores personalizados: 15
- Esquema de origem: `references/sentinel/logmanagement-schema.txt`

## Regra de caça
Antes de confiar em um resultado de busca, confirme a cobertura de dados com [Data Source Health](../sentinel/kql/daily/data-source-health.kql).
