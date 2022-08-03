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

Having well-defined guidelines in place can facilitate your software projects, especially more complex ones. But, you don’t necessarily need to invest the time and effort to document these practices from scratch. Instead, teams can leverage best practices documented by other reputable companies and adapt them for their own projects.

The Twelve-Factor App methodology has been around for a decade now. But, how relevant and important are these guidelines today? Here, we examine just how well they’ve held up in addressing architectural, deployment, and operational concerns in building software at scale.

The Twelve-Factor App, first presented around 2011, is a set of language-agnostic guidelines used to develop modern enterprise-grade software as a service. It promotes discipline in software development while addressing architectural, deployment, and operational concerns in building software at scale. While suitable for cloud-native applications, it works just as well with software of a similar nature that is hosted on-premises.

So, how does the Twelve-Factor App hold up today? Let’s review each of the twelve factors and see.

### 1. Codebase

A Twelve-Factor App requires code to be stored in source control (e.g., Git), and it defines the one-to-many relationship between a codebase and deploys (running instances of the app) resulting from it. It’s quite typical to have different versions of the app (from different commits) running in different environments.

Nowadays, the advantages of source control are well understood. Storing source code and its history centrally prevents accidents like lost code. This also facilitates many operations that have become a staple of software development, such as branching, merging, reverting changes, cherry-picking, and others. Thanks to well-established processes such as git-flow, even large teams can work on the same code concurrently.

### 2. Dependencies

Managing dependencies can be tricky, especially when they’re hidden or conflicting between apps. That’s why the Twelve-Factor App recommends declaring dependencies using the relevant programming language’s package manager. It also recommends that dependencies are packaged with the application rather than relying on system-wide dependencies or tools.

Declaring and isolating dependencies helps avoid conflicts between different applications that run on the same host but require different dependencies. Containers are a great way to package applications together with their dependencies, while at the same time abstracting the underlying environment and isolating them from each other.

### 3. Config

The Twelve-Factor App recognizes that while the same code is deployed across environments, the configuration is different for each environment. Therefore, the configuration should be strictly separated from code and stored in environment variables. This means that only one application build needs to be created which can be tested, deployed, and run in multiple environments.

The Twelve-Factor App doesn’t say how to store secrets, such as passwords or API tokens. And, while secrets can be thought of as configuration, their sensitive nature warrants special treatment. We recommend managing these using a secret management tool, such as HashiCorp Vault, AWS Secrets Manager, or any other valid tool in this category.

### 4. Backing Services

Any external dependency accessed over a network (e.g., an SQL or NoSQL database, API, SMTP service, etc.) should be specified in the application’s configuration. By simply changing the configuration, an external dependency should also be replaceable with a similar service.

### 5. Build, Release, Run

Taking a codebase and turning it into a running application in a particular environment involves the following stages:

The build stage uses the code and its dependencies to produce a build.
The release stage uses the build and its configuration to produce a release.
The run stage runs one or more instances of the release.
This process enables a clear separation of concerns and should be automated, using continuous integration and continuous deployment (CI/CD) pipelines. The CD part also maintains a history of deployments, making it easy to revert to an earlier version if necessary. Releases are generally immutable, so any change must create a new release.

Developer time is expensive and should not be wasted, so this process needs to be fast. Small optimizations that reduce the time it takes to build and deploy new code (e.g., faster builds, quality checks, or deployments) can have a big positive impact.

### 6. Processes

Apps and services should be stateless, with any state residing in a backing store. This is an important prerequisite for other Twelve-Factor guidelines, such as concurrency and disposability.

This approach provides important operational benefits, making it easier to scale and recover from failures. It’s also beneficial from a developer perspective: separating mutable data and side effects from logic makes the code deterministic, and, therefore, easier to test and parallelize.

### 7. Port Binding

Twelve-Factor Apps are self-contained and independent processes that do not run under the control of a parent process. They expose their services by listening on a port. This also means that they can act as backing services for other apps.

### 8. Concurrency

Twelve-Factor Apps can be scaled out by running multiple instances of the same application. Stateless processes are easy to spin up and down as necessary, either manually or automatically based on metrics or a schedule. At the same time, apps with isolated dependencies minimize the risk of issues when they run side by side on different hosts.

In this context, minimizing startup time means that the system can adapt more quickly to varying loads. This is another benefit of containers, which are lightweight and much quicker to boot up when compared to virtual machines.

### 9. Disposability

The Twelve-Factor App assumes that an application can go down at any time for any reason: elastically scaling resources to meet demand, hardware failures, or even intentional application restarts. Where possible, the app can gracefully dispose of any resources by handling an appropriate shutdown signal, like SIGTERM.

When designing apps around disposability, it helps if they are stateless. In that case, they only need to clean up the resources being used as part of request processing, as opposed to an in-memory state that could be expensive to replenish (e.g., cache). Minimizing startup time is also useful since running instances of an app can recover more quickly when they are physically relocated elsewhere.

### 10. Dev/Prod Parity

It is a matter of good discipline in software development (as well as operations) to keep different environments in sync. This includes:

Using the same type of backing software (e.g., databases) in both development and production.
Deploying frequently to minimize the gap between code in different environments.
Giving developers the responsibility to deploy and monitor their own applications, rather than having a separate operations team take care of this.
Although the Twelve-Factor App suggests that developers entirely take over operational responsibilities, in practice, this is not entirely necessary. It is quite common to have one or more DevOps engineers as part of a development team, ensuring those team goals are aligned across development and operational concerns, while at the same time making the best use of skill specialization.

### 11. Logs

The Twelve-Factor App is very clear that logs should be written to standard output and treated as an event stream. The application doesn’t care where logs are ultimately stored; it is up to the execution environment to pick them up and route them to the appropriate destination.

Conversely, an application that buffers logs in memory and periodically flushes them to a database is inherently flawed because:

It becomes coupled with the log storage, taking on additional dependencies to communicate with it, and the log storage can’t be changed without changing the application.
Log management has a direct and non-negligible impact on the application’s CPU and memory usage.
This is in violation of the process of being stateless.
Therefore, it is recommended to decouple the application from its log storage. It’s also imperative to avoid logging sensitive data, such as personally identifiable information or credentials.

### 12. Admin Processes

One-off processes like database migrations are an integral part of a release. Many of the points from the Twelve-Factor App itself also apply to these one-off processes. Such tasks are stored in the same codebase and released as part of the same release process.

However, under this point, The Twelve-Factor App also recommends using a REPL shell to “run arbitrary code or inspect the app’s models against the live database.” It also suggests using ssh to run arbitrary processes on production. We disagree with these approaches. For security and risk management reasons, all deploys should go through a proven CI/CD process and there should be no developer access to production.







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
