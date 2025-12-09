# Traefik - v3.6.4

**Release Name**: v3.6.4
**Published**: 2025-12-05T09:58:17Z
**Repository**: https://github.com/traefik/traefik

---

**CVE's fixed:**
- [CVE-2025-66490](https://nvd.nist.gov/vuln/detail/CVE-2025-66490) (Advisory [GHSA-gm3x-23wp-hc2c](https://github.com/traefik/traefik/security/advisories/GHSA-gm3x-23wp-hc2c))
- [CVE-2025-66491](https://nvd.nist.gov/vuln/detail/CVE-2025-66491) (Advisory [GHSA-7vww-mvcr-x6vj](https://github.com/traefik/traefik/security/advisories/GHSA-7vww-mvcr-x6vj))

**Important:** Please read the [migration guide](https://doc.traefik.io/traefik/v3.6/migrate/v3/#v364).

**Bug fixes:**
- **[server]** Reject suspicious encoded characters ([#12360](https://github.com/traefik/traefik/pull/12360) by [rtribotte](https://github.com/rtribotte))
- **[plugins]** Validate plugin module name ([#12291](https://github.com/traefik/traefik/pull/12291) by [kevinpollet](https://github.com/kevinpollet))
- **[http3]** Bump github.com/quic-go/quic-go to v0.57.1 ([#12319](https://github.com/traefik/traefik/pull/12319) by [GreyXor](https://github.com/GreyXor))
- **[http3]** Bump github.com/quic-go/quic-go to v0.57.0 ([#12308](https://github.com/traefik/traefik/pull/12308) by [GreyXor](https://github.com/GreyXor))
- **[server]** Bump golang.org/x/crypto to v0.45.0 ([#12296](https://github.com/traefik/traefik/pull/12296) by [kevinpollet](https://github.com/kevinpollet))
- **[acme]** Bump github.com/go-acme/lego/v4 to v4.29.0 ([#12333](https://github.com/traefik/traefik/pull/12333) by [ldez](https://github.com/ldez))
- **[k8s/ingress-nginx]** Fix SSL redirect to match NGINX behavior ([#12361](https://github.com/traefik/traefik/pull/12361) by [mmatur](https://github.com/mmatur))
- **[k8s/ingress-nginx]** Fix the service name for ingress-nginx provider ([#12352](https://github.com/traefik/traefik/pull/12352) by [mmatur](https://github.com/mmatur))
- **[k8s/ingress-nginx]** Fix nginx.ingress.kubernetes.io/proxy-ssl-verify annotation support ([#12351](https://github.com/traefik/traefik/pull/12351) by [rtribotte](https://github.com/rtribotte))
- **[middleware,authentication]** Change ForwardAuth error log level from DEBUG to ERROR ([#12324](https://github.com/traefik/traefik/pull/12324) by [murataslan1](https://github.com/murataslan1))

**Documentation:**
- **[api]** Fix typo in API dashboard configuration instructions ([#12335](https://github.com/traefik/traefik/pull/12335) by [NAICOLAS](https://github.com/NAICOLAS))
- **[docker]** Add documentation for loadbalancer.server.url in Docker and Swarm providers ([#12289](https://github.com/traefik/traefik/pull/12289) by [webash](https://github.com/webash))
- **[k8s/gatewayapi]** Fix links of Helm chart values reference to providers.kubernetesGateway.enabled ([#12315](https://github.com/traefik/traefik/pull/12315) by [shouhei](https://github.com/shouhei))
- **[k8s/ingress-nginx]** Fix default value of ingress-nginx provider in documentation ([#12328](https://github.com/traefik/traefik/pull/12328) by [mloiseleur](https://github.com/mloiseleur))
- **[k8s/ingress-nginx]** NGINX Ingress Controller to Traefik Migration Guide ([#12318](https://github.com/traefik/traefik/pull/12318) by [sheddy-traefik](https://github.com/sheddy-traefik))
- **[k8s/ingress-nginx]** Improve the configuration options display of the Kubernetes ingress-nginx provider ([#12297](https://github.com/traefik/traefik/pull/12297) by [mloiseleur](https://github.com/mloiseleur))
- **[k8s/ingress-nginx]** Improve ingress-nginx provider documentation ([#12288](https://github.com/traefik/traefik/pull/12288) by [sheddy-traefik](https://github.com/sheddy-traefik))
- **[service]** Fix loadbalancer doc for highest random weight ([#12283](https://github.com/traefik/traefik/pull/12283) by [ozon2](https://github.com/ozon2))
- Correctly Format the HTTP Service Documentation ([#12311](https://github.com/traefik/traefik/pull/12311) by [sheddy-traefik](https://github.com/sheddy-traefik))
- Add documentation about checkNewVersion ([#12298](https://github.com/traefik/traefik/pull/12298) by [darkweaver87](https://github.com/darkweaver87))

**Misc:**
- Merge branch v2.11 into v3.6 ([#12364](https://github.com/traefik/traefik/pull/12364) by [kevinpollet](https://github.com/kevinpollet))
- Merge branch v2.11 into v3.6 ([#12341](https://github.com/traefik/traefik/pull/12341) by [mmatur](https://github.com/mmatur))
- Merge branch v2.11 into v3.6 ([#12368](https://github.com/traefik/traefik/pull/12368) by [mmatur](https://github.com/mmatur))
