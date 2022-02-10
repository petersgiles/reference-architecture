---
title: "Maturity"
linkTitle: "Maturity"
weight: 4
description: >
  Maturity

---

## Overview

Broadly speaking, these factors contribute to four critical areas of modern software engineering:
• Continuous Integration/Deployment – automatically validate & deploy new code, build a single package for each path-to-production chain, etc.
• Monitoring/Observability – primarily through the focus on logs.
• Scalability – enable applications to support dynamic load increases through resource addition (and vice-versa), and by externalizing the system state & configuration.
• Technical Debt Management – through improved build/dependency debt management, and the emphasis on loosely-coupled architectures.
Solution Teams that demonstrate a good understanding of these concepts and allocate time and resources to addressing them in their product development are good candidates for strategic partnership.
First Pass Assessment Factors

Discussing these factors can reveal how prepare a solution is for multiple customer production level operations

## Factor Description

|#|Factor  |Description |
|--------------|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|I|Codebase|There should be exactly one codebase for a deployed service withthe codebase being used for many deployments.|
|II  |Dependencies |All dependencies should be declared, with no implicit reliance onsystem tools or libraries.|
|III |Config  |Configuration that varies between deployments should be stored inthe environment.|
|IV  |Backing services  |All backing services are treated as attached resources andattached and detached by the execution environment.|
|V|Build, release, run |The delivery pipeline should strictly consist of build, release,run. |
|VI  |Processes |Applications should be deployed as one or more stateless processeswith persisted data stored on a backing service.|
|VII |Port binding |Self-contained services should make themselves available to otherservices by specified ports. |
|VIII|Concurrency  |Concurrency is advocated by scaling individual processes.|
|IX  |Disposability|Fast startup and shutdown are advocated for a more robust andresilient system. |
|X|Dev/Prod parity|All environments should be as similar as possible.  |
|XI  |Logs |Applications should produce logs as event streams and leave theexecution environment to aggregate. |
|XII |Admin Processes|Any needed admin tasks should be kept in source control andpackaged with the application.|
|XIII|Observable|Apps should provide visibility about current health and metrics |
|XIV |Schedulable  |Applications should provide guidance on expected resourceconstraints. i.e. Kubernetes lets you configure request limits for thecontainers |
|XV  |Upgradable|Apps must upgrade data formats from previous generations |
|XVI |Least privilege|Containers and Services should be running with the leastprivilege. Every permission you allow should be thought of as a potentialattack |
|XVII|Auditable |Know what, when, who, and where for all critical operations|
|XVIII |Securable |Identity, Network, Scope, Certificates - Protect your app andresources from the outsiders|
|XIX |Measurable|Application usage should be measurable for quota or chargebacks |

## Examples of Good candidates for D2MSE

A vendor who has had a stable product for some time and is used by a few customers reliably.

They can create new instances of their service for new customers quickly and can recover from chaos and disaster quickly and reliably. This process is scripted for reliability and repeatability. Configuration is managed in the deployment environment.

There are clearly understood and monitored logging features that are streamed to an operations dashboard.
They have good relationships with their current customers and are now finding that the popularity of their product necessitates a bigger commitment of operational resources.  They know how to instantiate more instances of their product and are keen to leverage our expertise at running environments to let them focus on providing improved features for their customers.

There is a product team with members who have been involved since the product’s inception. They are adding new features but also burning down their technical debt. They are aware of the compromises they have made on the journey to market and have spent some time formulating plans to address these issues. They understand the underlying technologies they have built their system on and monitor those technologies for security advisories and other maintenance issues. They actively patch and upgrade their services and platforms to minimise risk to their customer base.

## Examples of Poor candidates for D2MSE

The product is completely new and hasn’t been used in a production environment by any customer. The project to create the software may still be underway and features are being presented to the project sponsor at a rapid pace. The team hasn’t yet developed any DevOps capability and is manually dropping changes in an environment that hasn’t been rebuilt since the project kicked off 12 months ago.

The product team has one person who has a vague idea of how to get the environment running. Nothing is documented and the run environments require constant attention from the product team. Senior members of the product team are often taken off the project to service other customers and the turn around on technical questions is not timely and getting their full attention is difficult.

Logging is done to files on the virtual machine instances host services rather than using backing services in the environment and there are no dashboards to give an overview of system health.

The solution is unable to scale, and jury-rigged fixes are put in place to get it over the line. Examples of this would be a message queue will be used hosted on the same server that hosts the solution’s web application to reduce processing load of long running requests.

The underlying technologies are not understood and there is no monitoring of changes in those technologies. Open-source projects that are no longer maintained are used as core components of the system.

The project isn’t even complete yet and already the technologies and languages used are several revisions behind. The team are trying to meet their project schedule deadlines so they can take a pay check and walk away from the engagement. There is no maintenance planned or resourced and there is already churn in the team.

## Chaos engineering – has anyone thought about what could go wrong

- Is my Frequently Asked Questions (FAQ) handbook rich enough to get solutions for most of the issues?
- Are my Standard Operating Procedures (SOPs) comprehensive and well tested to be able to help me when disaster strikes?
- How good are my Business Continuity Planning (BCP) and Disaster Recovery Planning (DRP) when a large outage happens?  - What would be my specific role in the coordination effort to manage the issues and get the apps back in prod?
- How good are my tools to spot and isolate impacted services and equipment?
- Are my prod applications categorized for criticality so that the SOPs and the recovery team could focus on the most - critical apps and services?
- Are my apps tested for security vulnerabilities?  How shielded are they from the vulnerabilities?
- Is my app security team involved in the architecture and design stage of the applications?  Did they do threat modelling - to build security into the application?
- How sensitive is my app security leadership to the OWASP  top threats published from time to time?  Do they make a - conscious effort to protect the applications from the threats that are relevant in my context?
- Is the Ops team trained and coached to look at chaos engineering as a positive step to protect the applications and - minimize disruptions rather than as an unwanted, overwhelming testing exercise?
- Is there an approach to move from simulated pre-prod testing to real chaos testing in production?  What would it take to - make such a progression?  Has my leadership made effort to train and coach the tech teams to build confidence in our - applications and infrastructure?
- Will I be made aware of a chaos engineering exercise at all? Ideally, I should be caught unawares and pushed to provide - quick support.
- Am I bound by the standard SLAs when a ‘new’ issue crops up because of the chaos engineering exercise?  Why not – that’s - part of the testing, isn’t it?
- Do we conduct chaos engineering in an integrated manner to randomly pull-down apps and infrastructure or do we conduct them in separate phases such as software services, servers, client machines, network devices, etc?
- How is my Site reliability engineering (SRE) team organized – is it structured as an SRE team per platform or portfolio - of applications or a separate SRE team for each application?  How will the SRE teams collaborate among themselves and - the Dev/architecture team during and after the chaos engineering exercise?
- Is the IT leadership willing to review the chaos engineering practices and tools to make it easy for me in Ops and all - others involved in building and maintaining the apps?
- And what about cloud-hosted applications? Is the cloud service provider an integral part of the chaos engineering - exercise?

## Signs of a Bad Business Partner

### Poor Communication

One sign that a partnership may not work is lack of communication. If communication isn’t clear or there is a delay in responses, then that is a sure sign that it’s best if the deal does not work out. Communication upfront will reveal a lot about what it will be like to work with the partner or vendor in the future, so don’t assume communication will get better if it’s not great from the start.
Unaligned Mission and Vision
Whether it is working with my team or a possible partnership, our mission/vision should always be aligned. There will be chaos and mismanagement if one of the people we work with goes a different route. If we’re not on the same path, we need to cancel the deal.

### Inconsistencies

The biggest warning sign when evaluating a prospective partner or vendor is inconsistencies. It’s true that vendors can be disingenuous at times because circumstances simply change due to conditions they cannot control. The key is to look closely at how they deal with change. Do they take a personal sacrifice, or are they perfectly fine with you absorbing the cost?

### Vague Answers

When you ask a question and can see certain parts of it are avoided even after asking numerous different ways, this could be a signal that something isn’t right. You want to work with a partner who directly answers you no matter what you are asking. Otherwise, the partner might be secretive or dishonest.

### Inflexibility

In today’s world, when dealing with partnerships there must be a win-win for both parties. If you’re looking to work with a vendor or partner who is not flexible and provides little guarantee or assurance of success for both sides, then it might be a risky endeavour. If you’re talking to a vendor, you’re the customer and they should be able to accommodate all reasonable requests.

### Lack of Responsibility

No one is perfect 100 percent of the time, and sometimes we slip up and make mistakes. However, if your partner, vendor, or anyone else on your team can’t admit they were wrong and point fingers at everyone else, it’s likely not the best fit. You need team members who hold themselves accountable so your business can grow and succeed, and this type of behaviour won’t get it there.

### Trash-Talking Others

If a prospective partner or vendor spends a lot of time trash-talking their competition or former clients, it’s a good sign that your partnership won’t work out. If this person is willing to trash-talk another business or client to someone they just met, they’re probably a difficult person to work with. Plus, if your partnership doesn’t work out, you’ll likely receive the same treatment.

### Not Respecting Your Time

A big red flag is if they do not respect my time. If they are late, miss a call, or reschedule a meeting last minute, then that tells me they probably aren’t a fit. Being lazy with one’s time means you don’t respect what they are doing, and you really don’t care. I pride myself on never being late and I expect the same back.

### Lack of Enthusiasm

If either you or your potential partner isn’t enthusiastic about a partnership, it’s likely a bad idea. A lack of enthusiasm can manifest itself as poor communication, cutting meetings and conversations short, or taking a long time to make decisions. A good partnership should generate excitement for both parties.
No Focus on Mutual Success
When there is a lack of focus on mutual success, then it’s going to be a one-way situation that is not conducive to a good partnership. They should be discussing benefits and goals from both points of view or it won’t work.

### A Focus on Grievances

A prospective business partner who talks excessively about grievances with past employers, colleagues, or partners is a cause for concern. Everyone does this to some degree, but a relentless focus on the negative is a red flag, a sign that perhaps the problem is not with the target of the complaints but the complainer.
Lack of Clarity on Deliverables
If you’re talking circles around one another in trying to define deliverables, you may not ever be able to pin this person down to laying everything out in black and white. That can work out for a partnership outside of business, but when it comes to responsibilities and money, everyone deserves to have the same understanding of deliverables.

### Rushing Things

When a prospective lead is far too eager to get started, the odds are high that it will only get worse when you have a working relationship. These are often the nightmarish micromanagers who will do everything last minute on their end and expect you to finish things “ASAP” on Friday at 5:57 p.m.

### Increased Focus on Competitors

If a meeting with a new vendor consists mostly of talk of their competitors, they’re most likely not confident in their own product or business. If they’re confident in what they’re producing, they’ll focus on themselves and what they can do to make it the best partnership possible.

### Lack of References

Any time we work with a new vendor, we should conduct background checks and check out references. If the company has a poor background check or/and can’t provide references from recent or current customers or partners, then we should move on.
