---
title: "There Is One Administrator"
linkTitle: "There Is One Administrator"
weight: 60
date: 2021-10-21
description: >
  There is no one person who knows everything and there are many things that could go wrong.
---

## The Problem

**There is no one person who knows everything.**

Well, this one seems obvious. Of course, there is no one person who knows everything. Is this a problem? As long as the application runs smoothly, it isn't. But, when something goes wrong, you'll need to fix it. Because so many people touched the app, the one who knows how to fix the problem might not be there.

**There are many things that could go wrong.**

One example is configuration. Today's applications store configurations in multiple stores: config files, environment variables, database, command line arguments. There is no one person that knows what is the effect of every possible config value.

Another thing that could go wrong is system upgrades. A distributed application has many moving parts and you need to make sure they are synchronized. For example, you need to make sure that the current version of the code works with the current version of the database. Nowadays there is a focus on DevOps and Continuous Delivery. But supporting zero downtime deployment is no easy feat.

But, at least these things are under your control. Many apps interact with 3rd party systems. This means that, if they go down, there isn't much that you can do. So, even if you had one administrator for your system, you still can't control 3rd party systems.

## Solutions

Everyone Should Be Responsible for the Release Process
This means involving Ops people or system administrators from the start. Ideally, they would be part of the team. Keeping the system administrator informed of your progress early on can help you spot constraints. For example, the production environment might have different configurations, security restrictions, firewall rules or available ports than a development environment.

### Logging and Monitoring

The systems administrators should have the right tools for error reporting and managing issues. You should think about monitoring from the start. Distributed systems should have centralized logging. Accessing logs on ten different servers to investigate an issue is not an acceptable approach.

### Decoupling

You should strive for the least amount of downtime during system upgrades. This means you should be able to upgrade different parts of the system independently. By making the components backward-compatible, you can update the server and the clients at different times.

By putting queues between components, you temporally decouple them. This means that, for example, the web server can still accept requests, even if the backend is down.

### Isolate Third-Party Dependencies

You should treat systems that are outside of your control differently than components that you own. This means making your system more resilient to 3rd party failures. You can reduce the impact of an outside dependency by introducing an abstraction layer. This means that when a 3rd party system fails, you'll have fewer places to look for bugs.

## Conclusion

To work around this fallacy, you need to make your system easy to manage. DevOps, logging and monitoring can help. You also need to think about the upgrade process of your system. You cannot deploy each sprint if the upgrade requires hours of downtime. There is no one administrator so everybody should be responsible for the release process.
