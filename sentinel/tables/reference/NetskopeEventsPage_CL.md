# NetskopeEventsPage_CL

## Objetivo de caça
Tabela personalizada Netskope usada para SASE, CASB, web, DLP, aplicativo e busca de rede.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `device` | `string` |
| `domain` | `string` |
| `dsthost` | `string` |
| `dstip` | `string` |
| `dst_location` | `string` |
| `forward_to_proxy_profile` | `string` |
| `hostname` | `string` |
| `http_transaction_count` | `int` |
| `log_file_name` | `string` |
| `sAMAccountName` | `string` |
| `severity` | `string` |
| `srcip` | `string` |
| `src_location` | `string` |
| `TimeGenerated` | `datetime` |
| `transactionid` | `string` |
| `url` | `string` |
| `user` | `string` |
| `useragent` | `string` |
| `userip` | `string` |
| `userkey` | `string` |
| `userPrincipalName` | `string` |
| `user_generated` | `string` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
NetskopeEventsPage_CL
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
NetskopeEventsPage_CL
| where TimeGenerated >= ago(24h)
| project device, domain, dsthost, dstip, dst_location, forward_to_proxy_profile, hostname, http_transaction_count
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `access_method` | `string` |
| `app` | `string` |
| `appcategory` | `string` |
| `app_sessionid` | `string` |
| `browser` | `string` |
| `browser_sessionid` | `string` |
| `browser_version` | `string` |
| `bypass_reason` | `string` |
| `bypass_traffic` | `string` |
| `category` | `string` |
| `cci` | `int` |
| `ccl` | `string` |
| `client_bytes` | `int` |
| `connectionid` | `string` |
| `conn_duration` | `int` |
| `conn_endtime` | `int` |
| `conn_starttime` | `int` |
| `CononicalName` | `string` |
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
| `dst_timezone` | `string` |
| `dst_zipcode` | `string` |
| `dynamic_classification` | `string` |
| `forward_to_proxy_profile` | `string` |
| `fromlogs` | `string` |
| `hostname` | `string` |
| `http_transaction_count` | `int` |
| `log_file_name` | `string` |
| `netskope_pop` | `string` |
| `network` | `string` |
| `numbytes` | `int` |
| `org` | `string` |
| `organization_unit` | `string` |
| `os` | `string` |
| `os_version` | `string` |
| `page` | `string` |
| `policy` | `string` |
| `protocol` | `string` |
| `requestid` | `string` |
| `req_cnt` | `int` |
| `resp_cnt` | `int` |
| `resp_content_len` | `int` |
| `resp_content_type` | `string` |
| `sAMAccountName` | `string` |
| `serial` | `string` |
| `server_bytes` | `int` |
| `sessionid` | `string` |
| `severity` | `string` |
| `sfwder` | `string` |
| `site` | `string` |
| `srcip` | `string` |
| `src_country` | `string` |
| `src_geoip_src` | `int` |
| `src_latitude` | `int` |
| `src_location` | `string` |
| `src_longitude` | `int` |
| `src_region` | `string` |
| `src_time` | `string` |
| `src_timezone` | `string` |
| `src_zipcode` | `string` |
| `ssl_decrypt_policy` | `string` |
| `suppression_end_time` | `int` |
| `suppression_start_time` | `int` |
| `TenantId` | `string` |
| `TimeGenerated` | `datetime` |
| `timestamp` | `int` |
| `traffic_type` | `string` |
| `transactionid` | `string` |
| `Type` | `string` |
| `type_s` | `string` |
| `url` | `string` |
| `ur_normalized` | `string` |
| `user` | `string` |
| `useragent` | `string` |
| `userip` | `string` |
| `userkey` | `string` |
| `userPrincipalName` | `string` |
| `user_generated` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
