# tsk-1428-pr-review-test

## Scope note: farewell authentication

This repository contains only a standalone `farewell(name)` formatter; it does not expose an HTTP endpoint or include an authentication layer. No authentication mechanism has been selected here because the owning service and security-team approval are unknown. Do not treat this utility or its tests as evidence that production calls are authenticated.

Human follow-up is required to identify the service that exposes the endpoint, confirm its approved authentication mechanism with the security team, then deploy the change and verify anonymous requests are denied against real production traffic.