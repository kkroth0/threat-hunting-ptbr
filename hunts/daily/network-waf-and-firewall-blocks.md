# Rede WAF e blocos de firewall

## Objetivo
Revise a atividade de rede bloqueada ou de alto risco através de firewall, telemetria WAF e SASE.

## Cadência
Caça Diária

## Tabelas Sentinel
- [CommonSecurityLog](../../sentinel/tables/reference/CommonSecurityLog.md)
- [Cloudflare_CL](../../sentinel/tables/reference/Cloudflare_CL.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)

## Ferramentas
- [Fortigate](../../tools/firewall/fortigate.md)
- [Cloudflare](../../tools/waf/cloudflare.md)
- [Netskope](../../tools/sase/netskope.md)

## KQL
[`daily/network-waf-and-firewall-blocks.kql`](../../sentinel/kql/daily/network-waf-and-firewall-blocks.kql)

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
