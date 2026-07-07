# Biblioteca CTH

Biblioteca de Cyber Threat Hunting centrada no Microsoft Sentinel.

Este repositório organiza o processo de hunting em torno de:

```text
Ferramenta ou plataforma -> tabela Sentinel -> entidade normalizada -> cenário de hunting -> KQL -> achado ou detecção
```

## Comece aqui
1. [Calendário de hunting](cadence/hunt-calendar.md)
2. [Cadência de hunting](cadence/README.md)
3. [Biblioteca de hunts](hunts/README.md)
4. [Catálogo de tabelas Sentinel](sentinel/tables/index.md)
5. [Biblioteca KQL](sentinel/kql/README.md)
6. [Casos de uso](use-cases/README.md)
7. [Pesquisa externa](external-research/README.md)
8. [Mapa de ferramentas e tabelas](sentinel/tables/tool-table-map.md)

## Seções principais
- [Cadência](cadence/README.md): processo diário, semanal, orientado por inteligência e mensal de hunting.
- [Hunts](hunts/README.md): páginas de cenário mapeadas para KQL, ferramentas e tabelas.
- [Casos de uso](use-cases/README.md): guia para transformar hunts em detecções Sentinel e casos de monitoramento.
- [Sentinel](sentinel/README.md): catálogo de tabelas, normalização de campos e biblioteca KQL.
- [Ferramentas](tools/README.md): ferramentas mapeadas para as tabelas Sentinel que elas alimentam.
- [Fontes de dados](data-sources/README.md): visões de telemetria de identidade, endpoint, rede, nuvem e SaaS.
- [Plataformas](platforms/README.md): contexto de nuvem e sistemas operacionais.
- [Metodologias](methodologies/README.md): PEAK, hipóteses, dados, inteligência, LATAM e hunting assistido por modelo.
- [Pesquisa externa](external-research/README.md): pesquisas públicas de hunting mapeadas para tabelas Sentinel locais, candidatos KQL e casos de uso.
- [Templates](templates/README.md): modelos reutilizáveis de páginas.
- [Scripts](scripts/README.md): scripts de suporte e notas de automação.

## Catálogo Sentinel atual
- Tabelas exclusivas com esquema: 45
- SIEM principal: Microsoft Sentinel
- Origem do esquema: `references/sentinel/logmanagement-schema.txt`

## Ritmo operacional
| Cadência | Objetivo |
| --- | --- |
| Hunt diário | Capturar risco ativo e confirmar a integridade dos dados. |
| Hunt semanal | Investigar baselines mais profundas e cenários recorrentes. |
| Hunt orientado por inteligência | Converter IOCs, TTPs e novas inteligências em buscas. |
| Hunt mensal | Melhorar cobertura, detecções, custo e roadmap. |
