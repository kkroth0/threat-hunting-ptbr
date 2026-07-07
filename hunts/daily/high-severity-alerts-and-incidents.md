# Alertas e incidentes de alta gravidade

## Objetivo
Revise detecções de alta prioridade e alertas de fornecedores que talvez ainda não tenham sido totalmente investigados.

## Cadência
Caça Diária

## Tabelas Sentinel
- [SecurityIncident](../../sentinel/tables/reference/SecurityIncident.md)
- [SecurityAlert](../../sentinel/tables/reference/SecurityAlert.md)
- [TrendMicro_XDR_WORKBENCH_CL](../../sentinel/tables/reference/TrendMicro_XDR_WORKBENCH_CL.md)
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)
- [NetskopeAlerts_CL](../../sentinel/tables/reference/NetskopeAlerts_CL.md)

## Ferramentas
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)
- [Trend Vision One](../../tools/edr/trend-vision-one.md)
- [Orca Security](../../tools/cspm/orca-security.md)
- [Netskope](../../tools/sase/netskope.md)

## KQL
[`daily/high-severity-alerts-and-incidents.kql`](../../sentinel/kql/daily/high-severity-alerts-and-incidents.kql)

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
