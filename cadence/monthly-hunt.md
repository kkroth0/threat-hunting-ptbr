# Caça mensal

## Objetivo
Melhorar o próprio programa de caça: cobertura, custo, qualidade de detecção e linhas de base.

## Timebox sugerido
Meio dia a um dia.

## Runbook
1. Revise a ingestão, a integridade do conector e as lacunas de cobertura.
2. Revise a qualidade dos alertas e incidentes.
3. Revise a linha de base da identidade e as tendências de atividades privilegiadas.
4. Revise o volume faturável e as tabelas barulhentas.
5. Atualize o roteiro de busca e o backlog.

## Consultas
- [`coverage-and-ingestion-review.kql`](../sentinel/kql/monthly/coverage-and-ingestion-review.kql)
- [`analytics-rule-and-incident-quality.kql`](../sentinel/kql/monthly/analytics-rule-and-incident-quality.kql)
- [`identity-baseline-review.kql`](../sentinel/kql/monthly/identity-baseline-review.kql)
- [`log-cost-and-billable-volume.kql`](../sentinel/kql/monthly/log-cost-and-billable-volume.kql)
