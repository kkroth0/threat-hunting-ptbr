# NetskopeEventsNetwork_CL

## Objetivo de caça
Tabela personalizada Netskope usada para SASE, CASB, web, DLP, aplicativo e busca de rede.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `action` | `string` |
| `device` | `string` |
| `domain` | `string` |
| `dsthost` | `string` |
| `dstip` | `string` |
| `dst_location` | `string` |
| `flow_status` | `string` |
| `hostname` | `string` |
| `sAMAccountName` | `string` |
| `srcip` | `string` |
| `src_location` | `string` |
| `TimeGenerated` | `datetime` |
| `user` | `string` |
| `userip` | `string` |
| `userkey` | `string` |
| `userPrincipalName` | `string` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
NetskopeEventsNetwork_CL
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
NetskopeEventsNetwork_CL
| where TimeGenerated >= ago(24h)
| project action, device, domain, dsthost, dstip, dst_location, flow_status, hostname
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `access_method` | `string` |
| `action` | `string` |
| `app` | `string` |
| `appcategory` | `string` |
| `category` | `string` |
| `cci` | `int` |
| `ccl` | `string` |
| `client_bytes` | `int` |
| `client_packets` | `int` |
| `count_i` | `int` |
| `device` | `string` |
| `domain` | `string` |
| `dsthost` | `string` |
| `dstip` | `string` |
| `dstport` | `int` |
| `dst_country` | `string` |
| `dst_geoip_src` | `int` |
| `dst_latitude` | `int` |
| `dst_location` | `string` |
| `dst_longitude` | `int` |
| `dst_region` | `string` |
| `dst_zipcode` | `string` |
| `end_time` | `string` |
| `flow_status` | `string` |
| `hostname` | `string` |
| `ip_protocol` | `string` |
| `netskope_pop` | `string` |
| `network_session_id` | `string` |
| `numbytes` | `int` |
| `num_sessions` | `int` |
| `organization_unit` | `string` |
| `os` | `string` |
| `os_version` | `string` |
| `policy` | `string` |
| `pop_id` | `string` |
| `protocol` | `string` |
| `protocol_port` | `string` |
| `publisher_cn` | `string` |
| `publisher_name` | `string` |
| `sAMAccountName` | `string` |
| `server_bytes` | `int` |
| `server_packets` | `int` |
| `session_duration` | `int` |
| `site` | `string` |
| `srcip` | `string` |
| `srcport` | `int` |
| `src_country` | `string` |
| `src_geoip_src` | `int` |
| `src_latitude` | `int` |
| `src_location` | `string` |
| `src_longitude` | `int` |
| `src_region` | `string` |
| `src_zipcode` | `string` |
| `start_time` | `string` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `timestamp` | `int` |
| `total_packets` | `int` |
| `traffic_type` | `string` |
| `tunnel_id` | `string` |
| `tunnel_type` | `string` |
| `tunnel_up_time` | `int` |
| `Type` | `string` |
| `type_s` | `string` |
| `ur_normalized` | `string` |
| `user` | `string` |
| `userip` | `string` |
| `userkey` | `string` |
| `userPrincipalName` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
