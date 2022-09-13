---
title: "Interaction"
linkTitle: "Interaction"
weight: 20
date: 2022-02-1
description: >
  ML Interaction
---

## Interaction Building Blocks

```mermaid
erDiagram

        ME ||--o{ IDENTITY : "has"
        IDENTITY||--|{ SYSTEM-ROLE : "has"
        IDENTITY||--o{ TASK : "requests"
        
        SYSTEM ||--|{ SYSTEM-ROLE : "defines"
        SYSTEM ||--|{ JOB : "schedules"
        SYSTEM ||--|{ OPERATION : "has"
                
        SYSTEM-ROLE ||--o{ SYSTEM-ROLE : "hierachy"
        SYSTEM-ROLE ||--o{ PERMISSION : "has"

        OPERATION ||--|| PERMISSION : "is a"
        OPERATION ||--|{ FUNCTION : "has"

        TASK ||--|{ OPERATION : "invokes"
        JOB ||--|{ TASK : "requests"
        

```

## ME

A Human who needs to use a System, a User.

## Identity

A token representing a User.

## System

A collection of operations that performs work.

## Operation

A collection of functionality.

## System-Role

A collection of operations that performs work.
