# Varredura de exposição à nuvem de alto risco

## Objetivo
Procure ativos de nuvem expostos, posturas arriscadas e atividades de acesso externo relacionadas a serviços públicos.

## Cadência
Caça Intelectual

## Tabelas Sentinel
- [OrcaAlerts_CL](../../sentinel/tables/reference/OrcaAlerts_CL.md)
- [AzureActivity](../../sentinel/tables/reference/AzureActivity.md)
- [Cloudflare_CL](../../sentinel/tables/reference/Cloudflare_CL.md)

## Ferramentas
- [Orca Security](../../tools/cspm/orca-security.md)
- [Microsoft Sentinel](../../tools/siem/microsoft-sentinel.md)
- [Cloudflare](../../tools/waf/cloudflare.md)

## KQL
[`intel/high-risk-cloud-exposure-sweep.kql`](../../sentinel/kql/intel/high-risk-cloud-exposure-sweep.kql)

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
