---
title: "Machine-Learning Ops Architecture"
linkTitle: "Machine-Learning Ops"
weight: 3
date: 2021-11-1
description: >
  Machine-Learning Ops Architecture - Delivering ML Models
---

## Introduction

Machine-Learning Operations (MLOps) seeks to deliver fresh and reliable AI products through continuous integration, continuous training and continuous delivery of machine learning systems. When new data becomes available, we update the AI model and deploy it (if improved) with DevOps practices. Azure DevOps pipelines support these practices and is the platform of choice.

AI or Machine Learning is however focused around AzureML, which has its pipeline and artifact system. The goal is to combine DevOps with AzureML pipelines in an end-to-end solution. We want to continuously train models and conditionally deploy them on our infrastructure and applications.


``` mermaid
flowchart TD

    classDef action fill:#D5E1A3,stroke:#333,stroke-width:1px;
    classDef trigger fill:#F1E8B8,stroke:#333,stroke-width:1px;
    classDef choice fill:#D1FAFF,stroke:#333,stroke-width:1px;
    classDef endzone fill:#E58F65,stroke:#333,stroke-width:1px;

    A(fa:fa-bolt Infrastructure Changed):::trigger
    D(fa:fa-bolt Function changed):::trigger
    F(fa:fa-bolt New Data):::trigger
    H[/done/]:::endzone

    subgraph PL1 [DevOps Infrastructure Pipeline]
        B[Terraform plan]:::action --> C[Terraform apply]:::action
    end

    subgraph PL2 [DevOps Function Pipeline]
        E[Deploy function]:::action
    end

    subgraph AML [Azure ML Pipeline]
        G{fa:fa-question Deploy Model}:::choice
    end

    A --> PL1 -->|redeploy| PL2
    D ---> PL2
    F --> AML

    AML -->|yes| PL2 --> H
    AML -->|no| H
```



## Principles

## Patterns

## Standards

## Reference Models

## Decision Framework
