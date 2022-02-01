---
title: "xDNA Building Blocks"
linkTitle: "Building Blocks"
weight: 50
date: 2022-02-2
description: >
  xDNA
---

## xDNA Building Blocks

```mermaid
erDiagram
          SITE ||--o{ SITE : "hierachy"
          SITE ||--o{ GEOMETRY : "has"
          SITE ||..|{ EQUIPMENT : "has"

          EQUIPMENT ||--|| ASSET : "is a"    

          ASSET ||--o{ ASSET-CONFIGURATION : "has"
          ASSET ||--o{ CLASSIFICATION : "has"

          CLASSIFICATION ||--|| TAG : "is a"
          TAG }|--|{ TAG : hierachy
          ASSET ||--o{ ASSEMBLY : "has"

          ASSEMBLY ||--|{ ASSEMBLY : "hierachy"
          ASSEMBLY ||--o{ COMPONENT : "has"

          SITE ||..|{ PERSON : "has"
          PERSON ||--o{ PERSON : "hierachy"
          PERSON ||..o{ ROLE : "has"
          PERSON ||..o{ QUALIFICATION : "has"

          ROLE ||--o{ ROLE : "hierachy"
          ROLE ||..o{ QUALIFICATION : "requires"

          QUALIFICATION ||--o{ QUALIFICATION : "hierachy"
          QUALIFICATION ||--|| TAG : "is a"
          QUALIFICATION ||--o{ EQUIPMENT : "is for"

```
