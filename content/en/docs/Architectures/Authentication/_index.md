---
title: "Authentication Reference Architecture"
linkTitle: "Authentication"
weight: 3
date: 2021-10-21
description: >
  Authentication Reference Architecture
---

## Introduction

- Across the world is an increasing level of technical interoperability required to enable parties to conduct business. Trust between parties is an essential part of life, human interaction depends on it.

- Maintaining a high level of trust with parties enables acceptance of various management standards, practices and policies, such as determination of identity, local authentication mechanisms, privileges and non-reputability of identifiers.

## Definition

- Authentication verifies who you are. It’s used to inform Access Control that enables the right entities to access the right resources at the right times, for the right reasons and in what ways.

> ‘The function for establishing the validity and assurance of a claimed identity of an entity in an information or communications system, by testing the credentials supplied by the entity making the claim/assertion’.

## Scope

- Authentication is relevant to multiple fields that cover both the logical aspects of technology and non-technology areas (for example physical assets).

- This Reference Architecture is only concerned with the technology areas that pertain to Authentication within our Organisation's Environment.

## Audience

- This document is for solution architects and capability planners. It is intended to guide and constrain technical solutions to fit within the overall enterprise. To fascilitate better communication parties should apply the language and concepts introduced here to ensure a consistent understanding.

## Overview

- Authentication is used to determine whether someone or something is, in fact who or what it is declared to be. Authentication may contribute towards access control; however, it is not the same.
- Authentication can be:
  - **Direct**. Interaction occurs inside the application boundary, without the need for an intermediary. If the shared secret between a requester and application is compromised, only the relationship between those two parties is compromised and not the entire model.
  - **Brokered**. Interaction occurs outside the boundary of the application, where an intermediary acts on behalf of an entity. An intermediary manages trust centrally, which eliminates the need for each entity and application to independently manage their own trust relationships. Examples of brokered authentication include Public Key Infrastructure, Kerberos, SAML, and OAuth.

### Federation

- Most modern applications have the potential to simplify authentication logic; these types don’t provide mechanisms for managing the identity lifecycle of an entity. Figure 1 shows that shifting the authentication layer outside the traditional model means that the application doesn’t hold onto sensitive data, therefore implies federation.

{{< figure src="figure01.png" title="Figure 1: Federation" >}}

- In technology, Federation implies linking a person’s electronic representation of an identity and attributes stored across multiple distinct systems. This provides collaboration capabilities across multiple applications that may be distributed across organisations, geographies or business units.

- Partners that interact with Defence may be subjected to further shifting of their token’s claims. This is due to the nature of the defined set of schemas which may contain existing attributes into the identity schema of an application. Other applications may contain variations of identity schemas which may introduce new attributes that are not specified. Therefore, the identity aggregation needs to know the attributes that are semantically equivalent to one another. Figure 2 represents the interaction of several autonomous units, with a greater need for interoperability.

{{< figure src="figure02.png" title="Figure 2: Identity schema" >}}

- Authentication techniques are used to validate an entity’s identity using identifiers based on various techniques, ranging from simple logon something the entity knows, to more complex mechanisms based on what the entity is, such as retinal pattern, hair colour or other biometric identifiers.

### Trust

- Skipping trust before authentication occurs introduces the risk of an agent to act under false identity. Technology enables capability which identifies identity mismatch patterns by scanning the agent before authentication occurs.
- Trust is one of the key elements in federation. Trust may vary; however, fundamentally it contains authentication between organisations that have established trust for shared access to a set of functions. Using Reference D, trust is determined by:
  - Level 1. Little or no confidence in the asserted identity’s validity.
  - Level 2. Some confidence in the asserted identity’s validity.
  - Level 3. High confidence in the asserted identity’s validity.
  - Level 4. Very high in the asserted identity’s validity.
- Authentication consists of various parts. Fundamentally, we care about:
  - Agent. Using Reference C, non-person entity, such as network-aware object, usually part of the Defence Information Environment. Facilitates interaction directly to the functionality of an application.
  - Function. Using Reference E: ‘A relation or expression involving one or more variables’. From an authentication point of view, we are talking about applications.
  - Identity Store. Repository that contains electronic representations of person and non-person entities.
- …
- Deployed nodes and levels of trust.

### Log On

- In order to verify an identity of an entity, various techniques known as personal identifiers may be used to confirm that identity. These include:
  - **Knowledge factors.** Something the person knows, such as password, pass phrase, personal identification number or challenge response.
  - **Ownership factors.** Something the person has, such as identification card or security token.
  - **Inherence factors.** Something the person is or does, such as fingerprint, retinal pattern, DNA sequence, facial or voice recognition.
- Entities are issued with credentials which are typically held by a third, trusted party, such as an authority. This provides establishment of the identity of an entity which may provide interaction, thus granting access to an application described as log on.
- Credentials are usually supplied as documentation, and may contain a key, personal identification number (PIN) or a phrase, are also commonly referred to as passwords. Credentials may be based entirely on knowledge techniques, or may be used in combination with ownership or inherence techniques to avoid another entity from assuming that identity.

## Principles

- The following principles are introduced to support this reference architecture:
  - Authentication must inform Access Control, therefore must operate within a contiguous unity.
  - Identity shall be invisible to the end user; identity, attribute verification and exchange should be a background operation until such time that increased levels of user verification is required.

## Reference Models

## Decision Framework

## Patterns
