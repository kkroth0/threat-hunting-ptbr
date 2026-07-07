# Endpoint suspeito PowerShell

## Objetivo
Encontre PowerShell suspeito e execução de script da telemetria Windows e XDR.

## Cadência
Caça Diária

## Tabelas Sentinel
- [SecurityEvent](../../sentinel/tables/reference/SecurityEvent.md)
- [WindowsEvent](../../sentinel/tables/reference/WindowsEvent.md)
- [TrendMicro_XDR_OAT_CL](../../sentinel/tables/reference/TrendMicro_XDR_OAT_CL.md)

## Ferramentas
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)
- [Trend Vision One](../../tools/edr/trend-vision-one.md)

## KQL
[`daily/endpoint-suspicious-powershell.kql`](../../sentinel/kql/daily/endpoint-suspicious-powershell.kql)

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
