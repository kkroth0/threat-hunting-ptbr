# Busca de mapeamento de tendência MITRE

## Objetivo
Pivô de mapeamentos de táticas ou técnicas ATT&CK em alertas de tendência e Sentinel.

## Cadência
Caça Intelectual

## Tabelas Sentinel
- [TrendMicro_XDR_OAT_CL](../../sentinel/tables/reference/TrendMicro_XDR_OAT_CL.md)
- [SecurityAlert](../../sentinel/tables/reference/SecurityAlert.md)

## Ferramentas
- [Trend Vision One](../../tools/edr/trend-vision-one.md)
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)

## KQL
[`intel/trend-mitre-mapping-hunt.kql`](../../sentinel/kql/intel/trend-mitre-mapping-hunt.kql)

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
