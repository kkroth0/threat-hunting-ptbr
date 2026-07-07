# Custo de registro e volume faturável

## Objetivo
Classifique o volume da tabela e o tamanho faturável para orientar a retenção, a análise e o ajuste de custos.

## Cadência
Caça Mensal

## Tabelas Sentinel
- [SigninLogs](../../sentinel/tables/reference/SigninLogs.md)
- [AuditLogs](../../sentinel/tables/reference/AuditLogs.md)
- [SecurityEvent](../../sentinel/tables/reference/SecurityEvent.md)
- [WindowsEvent](../../sentinel/tables/reference/WindowsEvent.md)
- [CommonSecurityLog](../../sentinel/tables/reference/CommonSecurityLog.md)
- [Cloudflare_CL](../../sentinel/tables/reference/Cloudflare_CL.md)
- [NetskopeAlerts_CL](../../sentinel/tables/reference/NetskopeAlerts_CL.md)
- [NetskopeEventsApplication_CL](../../sentinel/tables/reference/NetskopeEventsApplication_CL.md)
- [NetskopeEventsConnection_CL](../../sentinel/tables/reference/NetskopeEventsConnection_CL.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)
- [NetskopeEventsPage_CL](../../sentinel/tables/reference/NetskopeEventsPage_CL.md)
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)
- [TrendMicro_XDR_OAT_CL](../../sentinel/tables/reference/TrendMicro_XDR_OAT_CL.md)
- [TrendMicro_XDR_WORKBENCH_CL](../../sentinel/tables/reference/TrendMicro_XDR_WORKBENCH_CL.md)

## Ferramentas
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)

## KQL
[`monthly/log-cost-and-billable-volume.kql`](../../sentinel/kql/monthly/log-cost-and-billable-volume.kql)

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
