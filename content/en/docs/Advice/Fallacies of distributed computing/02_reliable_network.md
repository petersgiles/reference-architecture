---
title: "The Network Is Reliable"
linkTitle: "The Network Is Reliable"
weight: 20
date: 2021-10-21
description: >
  Calls over a network will fail.
---

## The Problem

Most of the systems today make calls to other systems. Are you integrating with 3rd party systems (payment gateways, accounting systems, CRMs)? Are you doing web service calls? What happens if a call fails? If you're querying data, a simple retry will do. But what happens if you're sending a command? Let's take a simple example:

```c#
var creditCardProcessor = new CreditCardPaymentService();
creditCardProcessor.Charge(chargeRequest);
```

What happens if we receive an HTTP timeout exception? If the server did not process the request, then we can retry. But, if it did process the request, we need to make sure we are not double charging the customer. You can do this by making the server idempotent. This means that if you call it 10 times with the same charge request, the customer will be charged only once. If you're not properly handling these errors, you're system is nondeterministic. Handling all these cases can get quite complex really fast.

### Solutions
So, if calls over a network can fail, what can we do? Well, we could automatically retry. Queuing systems are very good at this. They usually use a pattern called store and forward. They store a message locally, before forwarding it to the recipient. If the recipient is offline, the queuing system will retry sending the message. MSMQ is an example of such a queuing system.

But this change will have a big impact on the design of your system. You are moving from a request/response model to fire and forget. Since you are not waiting for a response anymore, you need to change the user journeys through your system. You cannot just replace each web service call with a queue send.

### Conclusion
You might say that networks are more reliable these days - and they are. But stuff happens. Hardware and software can fail - power supplies, routers, failed updates or patches, weak wireless signals, network congestion, rodents or sharks. Yes, sharks: Google is reinforcing undersea data cables with Kevlar after a series of shark bites.

And there's also the people side. People can start DDOS attacks or they can sabotage physical equipment.

Does this mean that you need to drop your current technology stack and use a messaging system? Probably not! You need to weigh the risk of failure with the investment that you need to make. You can minimize the chance of failure by investing in infrastructure and software. In many cases, failure is an option. But you do need to consider failure when designing distributed systems.
