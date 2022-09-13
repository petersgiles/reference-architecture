---
title: "IoT"
linkTitle: "IoT"
weight: 20
date: 2022-02-1
description: >
  xDNA IoT
---

## IoT Building Blocks

```mermaid
erDiagram
        SERVICE ||--o{ RESOURCE : "exposes"
        VIRTUAL-ENTITY ||--|{ RESOURCE : "associated"
        PHYSICAL-ENTITY ||--|| VIRTUAL-ENTITY : "represents"
        PHYSICAL-ENTITY ||--|{ DEVICE : "attached"
        DEVICE ||--|{ TELEMETRY : "streams"
        VIRTUAL-ENTITY ||--|{ TELEMETRY : "ingests"         

```
