---
title: "Latency Is Zero"
linkTitle: "Latency Is Zero"
weight: 10
date: 2021-10-21
description: >
 Calls over a network are not instant.
---

## The Problem

Calls over a network are not instant.
There is a seven-orders-of-magnitude difference between in-memory calls and calls over the internet. Your application should be network aware. This means you should clearly separate local calls from remote calls. Let's look over an example that I've seen in a codebase:

```c#
 var viewModel = new ViewModel();
 var documents = new DocumentsCollection();
 foreach (var document in documents)
 {
    var snapshot = document.GetSnapshot();
     viewModel.Add(snapshot);
}
```

Without further inspection, this looks fine. But, there are two remote calls. Line 2 makes one call to get a list of document summaries. At line 5 there is another call that retrieves more information about each document. This is a classic Select n+1 problem. In order to account for the network latency, you should return all the required data in one call. The general advice is that local calls can be fine-grained, but remote calls should be more coarse-grained. This is why the idea of distributed objects and "network transparency" died. But, even though everybody agrees that distributed objects are a bad idea, some people still think that lazy loading is always a good idea:

```c#
var employee = EmployeeRepository.GetBy(someCriteria)
var department = employee.Department;
var manager = department.Manager;
foreach (var peer in manager.Employees;)
{
    // do something
}
```

You wouldn't expect a property getter to do a network call. But, each "." call in the code above can trigger a trip to the database.

## Solutions

### Bring Back All the Data You Might Need

If you do a remote call, ensure that you bring back all the data you might need. Network communication should not be chatty.

### Move the Data Closer to the Clients

Another possible solution is to move the data closer to the clients. If you're using the cloud, choose the availability zone carefully, depending on your client's location. Caching can also help minimize the number of network calls. For static content, Content Delivery Networks (CDNs) are another good option.

### Invert the Flow of Data

Another option for removing the remote calls is to invert the flow of data. Instead of querying other services, we can use Pub/Sub and store the data locally. This way, we'll have the data when we need it. Of course, this introduces some complexity, but it can be a good tool in the toolbox.

## Conclusion

Although latency might not be an issue in LANs, when you move to WANs or the Internet, you'll notice the delay. This is why it's important for network calls to be separated from in-memory calls. You should keep this in mind when adopting the microservices architectural pattern. You shouldn't just replace local calls with remote calls. Chances are this will turn your system into a distributed big ball of mud.
