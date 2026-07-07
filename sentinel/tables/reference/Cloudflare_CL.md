# Cloudflare_CL

## Objetivo de caça
Tabela de log personalizada Cloudflare para WAF, edge, bot, request, origin e buscas de ação de segurança.

## Principais campos de caça
| Campo | Tipo |
| --- | --- |
| `CacheCacheStatus_s` | `string` |
| `CacheResponseStatus_d` | `real` |
| `ClientDeviceType_s` | `string` |
| `ClientIPClass_s` | `string` |
| `ClientIP_s` | `string` |
| `ClientMTLSAuthStatus_s` | `string` |
| `ClientRequestHost_s` | `string` |
| `ClientRequestUserAgent_g` | `string` |
| `ClientRequestUserAgent_s` | `string` |
| `Computer` | `string` |
| `EdgePathingStatus_s` | `string` |
| `EdgeRequestHost_s` | `string` |
| `EdgeResponseStatus_d` | `real` |
| `JA3Hash_g` | `string` |
| `JA3Hash_s` | `string` |
| `OriginResponseStatus_d` | `real` |
| `PayPerCrawlStatus_s` | `string` |
| `RequestHeaders_cf_access_user_s` | `string` |
| `ResponseHeaders_location_s` | `string` |
| `SecurityActions_s` | `string` |
| `SecurityAction_s` | `string` |
| `TimeGenerated` | `datetime` |
| `WebAssetsOperationID_g` | `string` |
| `WebAssetsOperationID_s` | `string` |
| `WorkerStatus_s` | `string` |
| `_ResourceId` | `string` |

## Consulta inicial
```kql
Cloudflare_CL
| where TimeGenerated >= ago(24h)
| summarize Events = count() by bin(TimeGenerated, 1h)
| order by TimeGenerated desc
```

## Projeção Rápida
```kql
Cloudflare_CL
| where TimeGenerated >= ago(24h)
| project CacheCacheStatus_s, CacheResponseStatus_d, ClientDeviceType_s, ClientIPClass_s, ClientIP_s, ClientMTLSAuthStatus_s, ClientRequestHost_s, ClientRequestUserAgent_g
| take 100
```

## Esquema Completo
| Campo | Tipo |
| --- | --- |
| `BotDetectionIDs_s` | `string` |
| `BotDetectionTags_s` | `string` |
| `BotScoreSrc_s` | `string` |
| `BotScore_d` | `real` |
| `BotTags_s` | `string` |
| `CacheCacheStatus_s` | `string` |
| `CacheReserveUsed_b` | `bool` |
| `CacheResponseBytes_d` | `real` |
| `CacheResponseStatus_d` | `real` |
| `CacheTieredFill_b` | `bool` |
| `ClientASN_d` | `real` |
| `ClientCity_s` | `string` |
| `ClientCountry_s` | `string` |
| `ClientDeviceType_s` | `string` |
| `ClientIPClass_s` | `string` |
| `ClientIP_s` | `string` |
| `ClientLatitude_s` | `string` |
| `ClientLongitude_s` | `string` |
| `ClientMTLSAuthCertFingerprint_s` | `string` |
| `ClientMTLSAuthStatus_s` | `string` |
| `ClientRegionCode_s` | `string` |
| `ClientRequestBytes_d` | `real` |
| `ClientRequestHost_s` | `string` |
| `ClientRequestMethod_s` | `string` |
| `ClientRequestPath_s` | `string` |
| `ClientRequestProtocol_s` | `string` |
| `ClientRequestReferer_s` | `string` |
| `ClientRequestScheme_s` | `string` |
| `ClientRequestSource_s` | `string` |
| `ClientRequestURI_s` | `string` |
| `ClientRequestUserAgent_g` | `string` |
| `ClientRequestUserAgent_s` | `string` |
| `ClientSrcPort_d` | `real` |
| `ClientSSLCipher_s` | `string` |
| `ClientSSLProtocol_s` | `string` |
| `ClientTCPRTTMs_d` | `real` |
| `ClientXRequestedWith_s` | `string` |
| `Computer` | `string` |
| `ContentScanObjResults_s` | `string` |
| `ContentScanObjSizes_s` | `string` |
| `ContentScanObjTypes_s` | `string` |
| `content_s` | `string` |
| `EdgeCFConnectingO2O_b` | `bool` |
| `EdgeColoCode_s` | `string` |
| `EdgeColoID_d` | `real` |
| `EdgeEndTimestamp_t` | `datetime` |
| `EdgePathingOp_s` | `string` |
| `EdgePathingSrc_s` | `string` |
| `EdgePathingStatus_s` | `string` |
| `EdgeRequestHost_s` | `string` |
| `EdgeResponseBodyBytes_d` | `real` |
| `EdgeResponseBytes_d` | `real` |
| `EdgeResponseCompressionRatio_d` | `real` |
| `EdgeResponseContentType_s` | `string` |
| `EdgeResponseStatus_d` | `real` |
| `EdgeServerIP_s` | `string` |
| `EdgeStartTimestamp_t` | `datetime` |
| `EdgeTimeToFirstByteMs_d` | `real` |
| `FirewallForAIInjectionScore_d` | `real` |
| `FirewallForAIPIICategories_s` | `string` |
| `FirewallForAITokenCount_d` | `real` |
| `FirewallForAIUnsafeTopicCategories_s` | `string` |
| `JA3Hash_g` | `string` |
| `JA3Hash_s` | `string` |
| `JA4Signals_browser_ratio_1h_d` | `real` |
| `JA4Signals_cache_ratio_1h_d` | `real` |
| `JA4Signals_h2h3_ratio_1h_d` | `real` |
| `JA4Signals_heuristic_ratio_1h_d` | `real` |
| `JA4Signals_ips_quantile_1h_d` | `real` |
| `JA4Signals_ips_rank_1h_d` | `real` |
| `JA4Signals_paths_rank_1h_d` | `real` |
| `JA4Signals_reqs_quantile_1h_d` | `real` |
| `JA4Signals_reqs_rank_1h_d` | `real` |
| `JA4Signals_uas_rank_1h_d` | `real` |
| `JA4_s` | `string` |
| `JSDetectionPassed_s` | `string` |
| `LeakedCredentialCheckResult_s` | `string` |
| `OriginDNSResponseTimeMs_d` | `real` |
| `OriginIP_s` | `string` |
| `OriginRequestHeaderSendDurationMs_d` | `real` |
| `OriginResponseBytes_d` | `real` |
| `OriginResponseDurationMs_d` | `real` |
| `OriginResponseHeaderReceiveDurationMs_d` | `real` |
| `OriginResponseHTTPExpires_s` | `string` |
| `OriginResponseHTTPLastModified_s` | `string` |
| `OriginResponseStatus_d` | `real` |
| `OriginResponseTime_d` | `real` |
| `OriginSSLProtocol_s` | `string` |
| `OriginTCPHandshakeDurationMs_d` | `real` |
| `OriginTLSHandshakeDurationMs_d` | `real` |
| `ParentRayID_s` | `string` |
| `PayPerCrawlStatus_s` | `string` |
| `RawData` | `string` |
| `RayID_s` | `string` |
| `RequestHeaders_cf_access_user_s` | `string` |
| `ResponseHeaders_location_s` | `string` |
| `SecurityActions_s` | `string` |
| `SecurityAction_s` | `string` |
| `SecurityRuleDescription_s` | `string` |
| `SecurityRuleIDs_s` | `string` |
| `SecurityRuleID_g` | `string` |
| `SecurityRuleID_s` | `string` |
| `SecuritySources_s` | `string` |
| `SmartRouteColoID_d` | `real` |
| `TimeGenerated` | `datetime` |
| `Type` | `string` |
| `UpperTierColoID_d` | `real` |
| `VerifiedBotCategory_s` | `string` |
| `WAFAttackScore_d` | `real` |
| `WAFFlags_s` | `string` |
| `WAFMatchedVar_s` | `string` |
| `WAFRCEAttackScore_d` | `real` |
| `WAFSQLiAttackScore_d` | `real` |
| `WAFXSSAttackScore_d` | `real` |
| `WebAssetsLabelsManaged_s` | `string` |
| `WebAssetsOperationID_g` | `string` |
| `WebAssetsOperationID_s` | `string` |
| `WorkerCPUTime_d` | `real` |
| `WorkerScriptName_s` | `string` |
| `WorkerStatus_s` | `string` |
| `WorkerSubrequestCount_d` | `real` |
| `WorkerSubrequest_b` | `bool` |
| `WorkerWallTimeUs_d` | `real` |
| `ZoneName_s` | `string` |
| `_BilledSize` | `real` |
| `_IsBillable` | `string` |
| `_ResourceId` | `string` |
| `_SubscriptionId` | `string` |
