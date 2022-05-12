# First Pass Assessment Quality Factors

Discussing these factors can reveal how prepared a solution is for multiple customer production level operations. This shouldn’t be considered a tick and flick pass or fail list. Solutions that achieve most of the Core Factors are more likely to be compatible with Cloud provisioned Infrastructure.
Core Factors

## Factor Description

| Num  | Title  | Description  |
|---|---|---|
|1 | Codebase |There should be exactly one codebase for a deployed service with the codebase being used for many deployments. |
|2 | Dependencies |All dependencies should be declared, with no implicit reliance on system tools or libraries. |
|3 | Config |The configuration that varies between deployments should be stored in the environment. |
|4 | Backing services |All backing services are treated as attached resources and attached and detached by the execution environment. |
|5 | Build, release, run |The delivery pipeline should strictly consist of build, release, run. |
|6 | Processes |Applications should be deployed as one or more stateless processes with persisted data stored on a backing service. |
|7 | Port binding |Self-contained services should make themselves available to other services by specified ports. |
|8 | Concurrency |Concurrency is advocated by scaling individual processes. |
|9 | Disposability |Fast start-up and shutdown are advocated for a more robust and resilient system. |
|10|  Dev/Prod parity |All environments should be as similar as possible. |
|11|  Logs |Applications should produce logs as event streams and leave the execution environment to aggregate. |
|12|  Admin Processes |Any needed admin tasks should be kept in source control and packaged with the application. |

### Bonus Factors for Consideration 

| Num  | Title  | Description  |
|---|---|---|
|13|  Observable |Apps should provide visibility about current health and metrics |
|14|  Schedulable |Applications should provide guidance on expected resource constraints. i.e., Kubernetes lets you configure request limits for the containers |
|15|  Upgradable |Apps must upgrade data formats from previous generations |
|16|  Least privilege |Containers and Services should be running with the least privilege. Every permission you allow should be thought of as a potential attack |
|17|  Auditable |Know what, when, who, and where for all critical operations |
|18|  Securable |Identity, Network, Scope, Certificates - Protect your app and resources from the outsiders |
|19|  Measurable |Application usage should be measurable for quota or chargebacks |
