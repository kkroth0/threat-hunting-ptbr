# HEARTH Mapeamento de Chamas

Esta pasta mapeia hipóteses de caça às chamas HEARTH para esta biblioteca de caça a ameaças Microsoft Sentinel.

Pasta de origem usada localmente: `/tmp/HEARTH/Flames`

Fonte canônica: [THORCollective HEARTH Chamas](https://github.com/THORCollective/HEARTH/tree/main/Flames)

## Arquivos gerados
- [Índice de Chamas](flames-index.md): HEARTH IDs, táticas, técnicas, tags e resumos de hipóteses compactas.
- [Mapa de chamas para Sentinel](flames-to-sentinel-map.md): tabelas Sentinel, ferramentas, candidatos KQL, candidatos de caso de uso, cadência e relevância LATAM para cada chama.
- [Rastreador de cobertura](coverage-tracker.md): status de cobertura, prioridade, iniciador KQL dedicado e notas de validação para cada Chama.
- [KQL Candidate Patterns](kql-candidate-patterns.md): padrões de design reutilizáveis Sentinel KQL para converter as Chamas mapeadas em caças funcionais.
- [Resumo da cobertura](coverage-summary.md): contagens de cobertura por domínio, tabela, cadência, técnica e relevância LATAM.
- [Iniciadores HEARTH KQL dedicados](../../sentinel/kql/hearth/README.md): um candidato inicial KQL gerado por Chama HEARTH.

## Escopo
- HEARTH Chamas mapeadas: 221
- Principais domínios mapeados: Endpoint e OS (200), Identidade e Acesso (144), Network Edge e SASE (120), Threat Intel e Detecções (119), Nuvem e Postura (74), Web e Application Edge (68)
- Principais tabelas Sentinel mapeadas: SecurityEvent (195), WindowsEvent (191), TrendMicro_XDR_OAT_CL (188), TrendMicro_XDR_WORKBENCH_CL (186), CommonSecurityLog (154), AuditLogs (140), SigninLogs (136), IdentityInfo (119)
- Fila de prioridade: P1 (25), P2 (114), P3 (76), P4 (6)
- Status de cobertura: Starter KQL - validar em Sentinel (198), Starter - validar telemetria SaaS (7), Starter - validar telemetria Linux (7), Parcial - ajuste personalizado necessário (5), Starter - validar telemetria de nuvem (4)

## Como usar
1. Escolha um HEARTH ID no mapa.
2. Confirme se as tabelas Sentinel mapeadas estão ingerindo dados.
3. Abra o starter HEARTH KQL dedicado ou o padrão reutilizável correspondente.
4. Valide a disponibilidade da tabela, os nomes dos campos, os limites e o comportamento comercial esperado.
5. Execute a busca com a linha de base do ambiente e o contexto LATAM.
6. Se o sinal se repetir com falsos positivos aceitáveis, crie um caso de uso a partir do [Modelo de caso de uso](../../templates/use-case-template.md).

## Notas
O mapeamento é uma camada de análise local. Ele resume o conteúdo HEARTH e vincula de volta à fonte original em vez de copiar as notas completas da fonte. Arquivos KQL dedicados são candidatos iniciais e ainda precisam de validação Sentinel antes da promoção de detecção.
