---
categories:
  - Class
tags: []
comment: null
info: null
date: 2016-9-9
type: post
layout: post
published: true
title: Grad Advanced Operating Systems & Distrib. Systems Notes
---
Professor Dave Andersen

# 2016-Sept-12 - Lecture 3
Admin: {Wed: Time, Clocks;  Fri: No Class}

- multithread individual programs to get crisp response.
- when you have 8+ cores, you need to think how to extract more parallelism. 
- in a modern multisocket there is two cpu's with a dram and a PCIe each (he calls them sockets b/c cpu's go in a  sockets), connected by a interconnect. Usually ~16 cores/cpu now. L1/L2 cache on core. L3 Cache per socket. (NUMA CPU Design). 
- bigger = slower means segregated memory hierachy (Physics) -> Time to activate a line and length of buses. 
- DRAM/CPU are different fab processes - expand at different rates, you dont want the mini metal interconnects to break as they expand
- HBM (high bandwidth memory) - stack of dram with a high bandwidth interconnect 
- Most cores can execute 2 threads at a time (hyperthreading)
- PCIe - peripherical connect interface -> attach flash / NIC / High speed peripheral interconnects to attach additional components.
- 

Q: Is DRAM always next to core on board?


# 2016-Sept-9 - Lecture 2 
- RPC
  - Have RPC look like local calls
  - synchronous calls
  - marshal args & copy to foreign server
  - SunRPC popularized RPC.
  - Encoding as JSON/BSON/XML
  - What if we do a remote call with f(a,b) where b is 10gb? > Design defined.
  - Decoupled Marshal from RPC (e.g. ZeroMQ with Protobuf serialization)
- How do we bind in modern day?
	- Zookeeper
- Failures
	- Exactly Once is impossible unless you have a reliable component e.g. hard drive - but not possible with just 
    - We focus on async communication because real networks are not synch and "life is hard"
- RPC System seems very interested in low level
    - Bypass Lower Layer OS network stack 
    - RDMA 
    - Cross-Layer Optimization
    
- RPC / General Message Passing used commonly now
- Distributed Transactional Memory possible over LAN not so much WAN.
