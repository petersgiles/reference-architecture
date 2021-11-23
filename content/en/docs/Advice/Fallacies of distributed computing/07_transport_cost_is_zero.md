---
title: "Transport Cost Is Zero"
linkTitle: "Transport Cost Is Zero"
weight: 70
date: 2021-10-21
description: >
  Transport cost is not zero.
---

## The Problem

This fallacy is related to the second fallacy, that latency is zero. Transporting stuff over the network has a price, in both time and resources. If the second fallacy discussed the time aspect, fallacy #7 tackles resource consumption.

There are two different sides of this fallacy:

### The Cost of the Networking Infrastructure

The networking infrastructure has a cost. Servers, SANs, network switches, load balancers and the people who take care of this equipment — all of these cost money. If your system is deployed on-premise, then you pay this price up front. If you're using the cloud, then you pay only for what you use, but you're still paying for it.

### The Cost of Serialization/Deserialization

The second aspect of this fallacy is the cost of transferring data between the transport level and the application level. Serialization and deserialization consume CPU time, so it costs money. If your app is deployed on-premise, this cost is somewhat hidden if you don't actively monitor resource consumption. But if your app is deployed in the cloud, this cost is painfully visible, since you're paying for what you use.

## Solutions

There isn't much you can do about the cost of infrastructure. You can only make sure that you're using it as efficiently as possible. SOAP or XML is more expensive than JSON. JSON is more expensive than binary protocols like Google's Protocol Buffers. Depending on the type of system, this can be more or less important. For example, the transport cost is much more important for apps that have to do with video streaming or VoIP.

## Conclusion

You should be mindful of the transport cost and how much serialization and deserialization your app is doing. This doesn't mean that you should optimize unless there is a need for it. You should benchmark and monitor resource consumption and decide if transport cost is a problem for you.
