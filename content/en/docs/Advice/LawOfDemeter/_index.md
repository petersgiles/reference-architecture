---
title: "Law of Demeter"
linkTitle: "Law of Demeter"
weight: 150
date: 2021-11-2
description: >
  Principle of Least Knowledge
---

Simply put, and assuming that you have a beautifully-crafted class that implements a given method, the method in question should be constrained to call other methods that belong to the following objects:

- An instance of the method’s originating class.
- Objects that are arguments of the target method.
- Objects that are created by the target method.
- Objects that are dependencies of the method’s originating class.
- Global objects (ouch!) that can be accessed by the originating class within the target method.

Although the list is a world away from being formal (for one that’s a little more formal, check out [Wikipedia](http://en.wikipedia.org/wiki/Law_of_Demeter)), the points are pretty easy to understand.

In traditional design, the fact that an object knows way too much about another (and this implicitly includes knowing how to access the third one) is considered wrong because there are situations where the object has to unnecessarily traverse from top to bottom a clumsy mediator to find the actual dependencies it needs to work as expected. This is, for obvious reason, a serious design flaw. The caller has detailed knowledge about the mediator’s internal structure, even if this one is accessed through a few getters.
