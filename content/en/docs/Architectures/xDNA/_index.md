---
title: "xDNA"
linkTitle: "xDNA"
weight: 3
date: 2021-11-1
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
          ROLE ||..o{ QUALIFICATION : "requires"
          QUALIFICATION ||--|| TAG : "is a"
          QUALIFICATION ||--o{ EQUIPMENT : "is for"

```

## Background

## Who should read this document?

## Principles

## Patterns

## Standards

## Reference Models

## Decision Framework
