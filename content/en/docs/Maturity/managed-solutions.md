# What is a Managed Solution Environment (MSE)?

Managed solutions provide hosted Software as a Service (SaaS), application services hosting platform environment to allow consumer business solutions for systems that process information up to and including the PROTECTED classification operated from Microsoft’s Azure platform. Unlike the Infrastructure as a Service (IaaS) offering provided by cloud service providers like Microsoft Azure, Amazon Web Services (AWS), and Vault Systems, the MSE takes care of not only the infrastructure hosting but also support, maintenance and consumer connectivity for the services and solutions it offers.

## Core Features

- Safe. The default deployment model ensures all data is replicated across multiple geographically
diverse datacentres and their deployment approach ensure the service can be reconstituted to an exact state if disaster strikes.
- Sovereign. The service and all its data are hosted and run within the Australian data centres by
an experienced and security cleared team.
- Secure. It is designed and built based on the Australian Government’s Information
Security Manual (ISM) and uses modern automation practices to manage deployment and
operations.
- Configuration as Code - All infrastructure is scripted as desired state configuration code and managed through source control.
- PaaS First – Where possible solutions are architected to prioritise the use of PaaS services.
- Repair by Replacement – Patching is not done in the ‘run’ environment, Solution Infrastructure is articulated as desired state configuration code. Environments are mutated by applying the desired state to the ‘run’ environment via agents and pipelines after change approval criteria are met.
- Privileged User Free / Hands off Operations – Operations staff have read-only access to the environment and monitor using aggregated logging dashboards. Admin (one-off) tasks are scripted and delivered via a change approval process. Solution Vendors and Users do not have access to hosted Solution infrastructure.

Compatible solutions would answer ‘No’ to the following Questions

- [ ] Does the solution require Cloud Infrastructure that is NOT available in Australian Datacentres?
- [ ] Does the solution require access that breaches the ISM guidelines?
- [ ] Does the solution require patching in the ‘run’ environment?
- [ ] Does the solution require interactive Admin access in the ‘run’ environment?

## Solution Compatibility Overview

Broadly speaking, these factors contribute to four critical areas of modern software engineering:

- Continuous Integration/Deployment – automatically validate & deploy new code, build a single package for each path-to-production chain, etc.
- Monitoring/Observability – primarily through the focus on logs.
- Scalability – enable applications to support dynamic load increases through resource addition (and vice-versa), and by externalizing the system state & configuration.
- Technical Debt Management – through improved build/dependency debt management, and the emphasis on loosely-coupled architectures.

Solution Vendor Teams that demonstrate a good understanding of these concepts and allocate time and resources to addressing them in their product development are good candidates for strategic partnership.
