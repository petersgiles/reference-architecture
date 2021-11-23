---
title: "Making MLOps easy for End-Users"
linkTitle: "Easy MLOps"
weight: 3
date: 2021-11-1
description: >
  A tutorial on simplifying MLOps using open source tools
---

## Purpose

An MLOps framework must come with batteries included and support an extensive list of features; model lifecycle management and governance, monitoring, A/B testing, interpretability, drift/outlier detection, and so on. 

However, as a data scientist:

> I just want to define a given python interface, push a big green button, and get a REST endpoint URL where I can interact with my deployed model.

We want to put all these models into a simple python class, which we want to register into the [mlflow](https://mlflow.org/) model registry. Essentially we want this class to do everything; return predictions, return explanations, define metrics to monitor, etc.
