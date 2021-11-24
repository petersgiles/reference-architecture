---
title: "The Network Is Homogeneous"
linkTitle: "The Network Is Homogeneous"
weight: 80
date: 2021-10-21
description: >
   The network is not homogenous.
---

## The Problem

A homogenous network is a network of computers using similar configurations and the same communication protocol. Having computers with similar configurations is a hard task to achieve. For example, you have little control over what mobile devices can connect to your app. This is why it's important to focus on standard protocols.

## Solutions

You should choose standard formats in order to avoid vendor lock-in. This might mean XML, JSON or Protocol Buffers. There are plenty of options to choose from.

## Conclusion

You need to ensure that the system's components can talk with each other. Using proprietary protocols will damage your app's interoperability.

Designing Distributed Systems Is Hard
These fallacies were published more than 20 years ago. But they still hold true today, some of them more than others. I think that many developers today know them, but the code that we write doesn't show this.

We must accept these as facts: the network is unreliable, insecure and costs money. Bandwidth is limited. The network's topology will change. Its components are not configured the same way. Being aware of these limitations will help us design better distributed systems.
