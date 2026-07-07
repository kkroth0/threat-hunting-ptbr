# Revisão de cobertura e ingestão

## Objetivo
Revise se as fontes de dados esperadas ainda estão enviando logs e se a ingestão mudou materialmente.

## Cadência
Caça Mensal

## Tabelas Sentinel
- [Usage](../../sentinel/tables/reference/Usage.md)
- [Heartbeat](../../sentinel/tables/reference/Heartbeat.md)
- [SentinelHealth](../../sentinel/tables/reference/SentinelHealth.md)

## Ferramentas
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)

## KQL
[`monthly/coverage-and-ingestion-review.kql`](../../sentinel/kql/monthly/coverage-and-ingestion-review.kql)

## Fluxo de trabalho do analista
1. Confirme a integridade da fonte de dados nas tabelas acima.
2. Execute KQL com o lookback padrão.
3. Revise as principais entidades, valores discrepantes e padrões repetidos.
4. Enriqueça usuários, hosts, IPs, URLs, hashes ou recursos de nuvem suspeitos.
5. Registre a decisão: benigna, suspeita, incidente, candidato a detecção ou item de ajuste.

## Resultado Esperado
- Descobertas confirmadas ou falsos positivos documentados.
- Notas de ajuste para limites, listas de permissões, listas de observação ou melhorias no analisador.
- Detecção ou acompanhamento de incidentes quando o comportamento se repete ou apresenta impacto.
