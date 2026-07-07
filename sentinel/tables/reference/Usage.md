# Usage

## Objetivo de caça
Registros de uso do espaço de trabalho para ingestão, dados faturáveis e revisão de cobertura de fonte de dados.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `Computer` | `string` |
| `LinkedResourceUri` | `string` |
| `ResourceUri` | `string` |
| `TimeGenerated` | `datetime` |

## Consulta inicial
```kql
Usage
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
Usage
| where TimeGenerated >= ago(24h)
| project Computer, LinkedResourceUri, ResourceUri, TimeGenerated
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AvgLatencyInSeconds` | `real` |
| `BatchesCapped` | `long` |
| `BatchesOutsideSla` | `long` |
| `BatchesWithinSla` | `long` |
| `Computer` | `string` |
| `DataType` | `string` |
| `EndTime` | `datetime` |
| `IsBillable` | `bool` |
| `LinkedMeterId` | `string` |
| `LinkedResourceUri` | `string` |
| `MeterId` | `string` |
| `Plan` | `string` |
| `Quantity` | `real` |
| `QuantityUnit` | `string` |
| `ResourceUri` | `string` |
| `Solution` | `string` |
| `SourceSystem` | `string` |
| `StartTime` | `datetime` |
| `TimeGenerated` | `datetime` |
| `TotalBatches` | `long` |
| `Type` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
