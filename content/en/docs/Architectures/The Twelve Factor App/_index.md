---
title: "The Twelve Factor App"
linkTitle: "The Twelve Factor App"
weight: 3
date: 2021-10-21
description: >
  The Twelve Factor App
---

## Introduction

In the modern era, software is commonly delivered as a service: called web apps, or software-as-a-service. The twelve-factor app is a methodology for building software-as-a-service apps that:

Use declarative formats for setup automation, to minimize time and cost for new developers joining the project;
Have a clean contract with the underlying operating system, offering maximum portability between execution environments;
Are suitable for deployment on modern cloud platforms, obviating the need for servers and systems administration;
Minimize divergence between development and production, enabling continuous deployment for maximum agility;
And can scale up without significant changes to tooling, architecture, or development practices.
The twelve-factor methodology can be applied to apps written in any programming language, and which use any combination of backing services (database, queue, memory cache, etc).

## Background

This document synthesizes the experience and observations on a wide variety of software-as-a-service apps in the wild. It is a triangulation on ideal practices for app development, paying particular attention to the dynamics of the organic growth of an app over time, the dynamics of collaboration between developers working on the app’s codebase, and avoiding the cost of software erosion.

Our motivation is to raise awareness of some systemic problems we’ve seen in modern application development, to provide a shared vocabulary for discussing those problems, and to offer a set of broad conceptual solutions to those problems with accompanying terminology. The format is inspired by Martin Fowler’s books Patterns of Enterprise Application Architecture and Refactoring.

## Who should read this document?

Any developer building applications which run as a service. Ops engineers who deploy or manage such applications.

## Principles

## Patterns

## Standards

## Reference Models

## Decision Framework
