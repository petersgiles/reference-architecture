---
title: "The Network Is Secure"
linkTitle: "The Network Is Secure"
weight: 40
date: 2021-10-21
description: >
  The network is insecure.
---

## The Problem

This is one assumption that gets more media coverage than the others. Your system is only as secure as your weakest link. The bad news is that there are a lot of links in a distributed system. You're using HTTPS, except when communicating with that 3rd party legacy system that doesn't support it. You're reviewing your own code, looking for security issues, but are using open source libraries that might be a risk. An OpenSSL vulnerability allowed people to steal data protected by SSL/TLS. A bug in Apache Struts allowed attackers to execute code on the server. Even if you're protecting against all of that, there still is the human factor. A malicious DBA can "misplace" a database backup. The attackers of today have a lot of computing power in their hands and a lot of patience. So the question is not if they're going to attack your system, but when.

## Solutions

### Defense in Depth

You should use a layered approach to secure your system. You need different security checks at the network, infrastructure and application level.

### Security Mindset

Keep security in mind when designing your system. The top ten vulnerabilities list has not changed that much in the last 5 years. You should follow best practices for secure software design and review code for common security flaws. You should regularly search 3rd party libraries for new vulnerabilities. The list of Common Vulnerabilities and Exposures can help.

### Threat Modeling

Threat modeling is a systematic approach of identifying possible security threats in a system. You first identify all the assets in your system (user data in the database, files, etc) and how they are accessed. After that, you identify possible attacks and start executing them. I recommend reading Chapter 2 in Advanced API Security for a good overview of Threat Modelling.

## Conclusion

The only secure system is one that is powered off, not connected to any network (and ideally cast in a block of concrete). What a useful system that it! The truth is that security is hard and expensive. There are a lot of components and links in a distributed system and each one of them is a possible target for malicious users. The business needs to balance the risk and probability of an attack with the cost of implementing prevention mechanisms.

Attackers have a lot of patience and computing power at their hands. We can prevent certain types of attacks by using threat modeling, but we can't guarantee 100% security. So it's a good idea to make this clear to the business, decide together how much to invest in security and have a plan for when a security breach does happen.
