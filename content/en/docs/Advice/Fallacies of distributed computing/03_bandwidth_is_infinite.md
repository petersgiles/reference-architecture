---
title: "Bandwidth Is Infinite"
linkTitle: "Bandwidth Is Infinite"
weight: 30
date: 2021-10-21
description: >
  Bandwidth is limited.
---

## The Problem

Bandwidth is the capacity of a network to send data over a period of time. Up until now, I've not found it to be a problem, but I can see why it could be an issue in certain conditions. Although bandwidth has improved over time, the amount of data that we send has increased too. Video streaming or VoIP will need more bandwidth than apps that are passing simple DTOs over the network. Bandwidth is even more important for mobile apps, so developers need to think about it when designing their backend APIs.

Using an ORM incorrectly can hurt too. I've seen examples of developers calling .ToList() too early in a query, thus loading an entire table in memory.

## Solutions

### Domain-Driven Design Patterns

So how can we make sure we don't bring too much data? Domain-Driven Design patterns can help:

First, you should not strive for a single, enterprise-wide domain model. You should partition your domain into bounded contexts.

To avoid large and complex object graphs inside a bounded context, you could use the Aggregate pattern. Aggregates ensure consistency and define transactional boundaries.

### Command and Query Responsibility Segregation

We sometimes load complex object graphs because we need to display parts of it on a screen. If we do this in lots of places, we end up with a large and complicated model that is suboptimal for both writing and reading. Another approach could be to use Command and Query Responsibility Segregation - CQRS. This means splitting the domain model in two:

The write model will ensure invariant hold true and the data is consistent. Since the write model doesn't care about view concerns, it can be kept small and focused.
The read model is optimized for view concerns, so we can retrieve all the data that is required for a specific view (e.g. a screen in our app).

## Conclusion

There is a tension between the second fallacy, latency is not 0, and the third fallacy, bandwidth is infinite. You should transfer more data to minimize the number of network round trips. You should transfer less data to minimize bandwidth usage. You need to balance these two forces and find the right amount of data to send over the wire.

Although you might not hit the bandwidth limitation often, thinking about the data that you transfer is important. Less data is easier to understand. Less data means less coupling. So transfer only the data that you might need.
