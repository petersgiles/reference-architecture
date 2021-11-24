---
title: "Topology Doesn't Change"
linkTitle: "Topology Doesn't Change"
weight: 50
date: 2021-10-21
description: >
  Network topologies change constantly.
---

## The Problem

Network topology changes all the time. Sometimes it changes for accidental reasons - when your app server goes down and you need to replace it. Many times it's deliberate — adding new processes on a new server. Nowadays, with cloud and containers on a rise, this is even more visible. Elastic scaling - the ability to add or remove servers depending on the workload - requires a certain degree of network agility.

## Solutions

Abstract the Physical Structure of the Network
The first thing you need to do is to abstract the physical structure of the network. There are several ways in which you can do that:

### Stop hardcoding IPs

You should prefer using hostnames. By using URIs we are relying on the DNS to resolve the hostname to an IP.

When DNS is not enough (e.g. when you need to map an IP and a port), then use discovery services.
Service Bus frameworks can also provide location transparency.
Cattle, Not Pets
By treating your servers as cattle, not pets you are ensuring that no server is irreplaceable. This bit of wisdom helps you get into the right mindset: any server can fail (thus changing the topology), so you should automate as much as you can.

### Test

One last piece of advice is to test your assumptions. Stop a service or shut down a server and see if your system is still up and running. Tools like Netflix's Chaos Monkey take this up a notch, by randomly shutting down VMs or containers in your production environment. By bringing the pain forward, you are more motivated to build a more resilient system that can handle topology changes.

## Conclusion

Ten years ago, most topologies didn't change that often. But when it did, it probably happened in production and introduced some downtime. Nowadays, with cloud and containers on the rise, it's hard to ignore this fallacy. You need to be prepared for failure and test for it. Don't wait for it to happen in production!
