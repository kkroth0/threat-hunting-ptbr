# Watchlist

## Objetivo de caça
Registros de lista de observação Sentinel para listas de permissões, contexto de negócios, listas IOC e enriquecimento.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `TimeGenerated` | `datetime` |
| `_DTItemStatus` | `string` |

## Consulta inicial
```kql
Watchlist
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
Watchlist
| where TimeGenerated >= ago(24h)
| project TimeGenerated, _DTItemStatus
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `AzureTenantId` | `string` |
| `CorrelationId` | `string` |
| `CreatedBy` | `dynamic` |
| `CreatedTimeUTC` | `datetime` |
| `DefaultDuration` | `string` |
| `EntityMapping` | `dynamic` |
| `LastUpdatedTimeUTC` | `datetime` |
| `Notes` | `string` |
| `Provider` | `string` |
| `SearchKey` | `string` |
| `Source` | `string` |
| `SourceSystem` | `string` |
| `Tags` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `TimeToLive` | `datetime` |
| `Type` | `string` |
| `UpdatedBy` | `dynamic` |
| `WatchlistAlias` | `string` |
| `WatchlistCategory` | `string` |
| `WatchlistId` | `string` |
| `WatchlistItem` | `dynamic` |
| `WatchlistItemId` | `string` |
| `WatchlistName` | `string` |
| `_BilledSize` | `real` |
| `_DTItemId` | `string` |
| `_DTItemStatus` | `string` |
| `_DTItemType` | `string` |
| `_DTTimestamp` | `datetime` |
| `_IsBillable` | `string` |
