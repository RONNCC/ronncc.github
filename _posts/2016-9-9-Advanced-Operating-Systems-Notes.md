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
> Wed: Time, Clocks
> Fri: No Class



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
