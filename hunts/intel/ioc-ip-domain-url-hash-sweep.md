# IOC IP Domínio URL Varredura de hash

## Objetivo
Combine dados observáveis de inteligência de ameaças ativas com telemetria de rede, endpoint, nuvem e fornecedor.

## Cadência
Caça Intelectual

## Tabelas Sentinel
- [ThreatIntelIndicators](../../sentinel/tables/reference/ThreatIntelIndicators.md)
- [CommonSecurityLog](../../sentinel/tables/reference/CommonSecurityLog.md)
- [Cloudflare_CL](../../sentinel/tables/reference/Cloudflare_CL.md)
- [NetskopeAlerts_CL](../../sentinel/tables/reference/NetskopeAlerts_CL.md)
- [NetskopeEventsApplication_CL](../../sentinel/tables/reference/NetskopeEventsApplication_CL.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)
- [TrendMicro_XDR_OAT_CL](../../sentinel/tables/reference/TrendMicro_XDR_OAT_CL.md)
- [TrendMicro_XDR_WORKBENCH_CL](../../sentinel/tables/reference/TrendMicro_XDR_WORKBENCH_CL.md)
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)

## Ferramentas
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)
- [Fortigate](../../tools/firewall/fortigate.md)
- [Cloudflare](../../tools/waf/cloudflare.md)
- [Netskope](../../tools/sase/netskope.md)
- [Trend Vision One](../../tools/edr/trend-vision-one.md)
- [Orca Security](../../tools/cspm/orca-security.md)

## KQL
[`intel/ioc-ip-domain-url-hash-sweep.kql`](../../sentinel/kql/intel/ioc-ip-domain-url-hash-sweep.kql)

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
