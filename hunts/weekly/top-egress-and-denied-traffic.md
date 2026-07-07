# Principais saídas e tráfego negado

## Objetivo
Volume de saída de linha de base, destinos, usuários e atividade de rede bloqueada.

## Cadência
Caça Semanal

## Tabelas Sentinel
- [CommonSecurityLog](../../sentinel/tables/reference/CommonSecurityLog.md)
- [NetskopeEventsNetwork_CL](../../sentinel/tables/reference/NetskopeEventsNetwork_CL.md)
- [Cloudflare_CL](../../sentinel/tables/reference/Cloudflare_CL.md)

## Ferramentas
- [Fortigate](../../tools/firewall/fortigate.md)
- [Netskope](../../tools/sase/netskope.md)
- [Cloudflare](../../tools/waf/cloudflare.md)

## KQL
[`weekly/top-egress-and-denied-traffic.kql`](../../sentinel/kql/weekly/top-egress-and-denied-traffic.kql)

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
