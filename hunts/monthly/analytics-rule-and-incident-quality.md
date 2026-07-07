# Regra de análise e qualidade de incidente

## Objetivo
Revise as detecções de ruído, o ciclo de vida do incidente, a propriedade e a qualidade do fechamento.

## Cadência
Caça Mensal

## Tabelas Sentinel
- [SecurityIncident](../../sentinel/tables/reference/SecurityIncident.md)
- [SecurityAlert](../../sentinel/tables/reference/SecurityAlert.md)
- [SentinelAudit](../../sentinel/tables/reference/SentinelAudit.md)

## Ferramentas
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)

## KQL
[`monthly/analytics-rule-and-incident-quality.kql`](../../sentinel/kql/monthly/analytics-rule-and-incident-quality.kql)

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
