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
Paper: Using Threads in Interactive Systems: A Case Study Hauser 93 SIGOPS


## Precursor

- multithread individual programs to get crisp response.
- when you have 8+ cores, you need to think how to extract more parallelism. 
- in a modern multisocket there is two cpu's with a dram and a PCIe each (he calls them sockets b/c cpu's go in a  sockets), connected by a interconnect. Usually ~16 cores/cpu now. L1/L2 cache on core. L3 Cache per socket. (NUMA CPU Design). 
- bigger = slower means segregated memory hierachy (Physics) -> Time to activate a line and length of buses. 
- DRAM/CPU are different fab processes - expand at different rates, you dont want the mini metal interconnects to break as they expand
- HBM (high bandwidth memory) - stack of dram with a high bandwidth interconnect 
- Most cores can execute 2 threads at a time (hyperthreading)
- PCIe - peripherical connect interface -> attach flash / NIC / High speed peripheral interconnects to attach additional components.
- > 1000's of threads to keep cores 100% utilized
- more energy efficient to buy 2x the cpu's but things like huffman encoding because not parallelizable



## Process vs Thread (in context of paper) 

- Process has Seperate Address space vs Shared (Thread)
- Process have own resources & permissions whereas Threads share those e.g. open file descriptors
- Threads are cheaper (not cheap!). ~ 100kb in this, Processes are (~10s of MB).
	- Fibers/Coroutines: "Fiber is smaller than a thread". Within a process cooperatively process & multischedule. can have 10/100k of these.
- Preemptive vs Cooperative Threads (os steps in vs thread runs till it gives up control)
- A process switch requires interrupts, and then run a OS scheduler, and then returning control potentially to a different process: the most expensive thing is to invalidate the TLB :( . 
- Threads require interrupt but doesnt invalidate TLB
- Application Schedulers on the other hand - Function call, table lookup, function call -> much much cheaper. 
	- e.g. Fiber schedulers are app level schedulers.
- "Rob Pike from the Go team" has a great talk on using gothreads to write a compiler

## Paper 
- Mark Weiser (an author): one of fathers of ubiquitous computing 
- Kinds of Threads:
	- Transient:
    	- Defer: Another thread to do long tasks
        - Pump: Input transformer
        - Sleeper (time/periodic)
        - Slack  (e.g. batching=less work/more efficient). But slack process /w wrong thread priority / not many things to do is degrading of performance. Also possibility for priority inversion. 
        	- Ways to attempt to reduce deadlock: Deadlock Checker Thread / Have a thread give up all locks and try to get all of them from scratch. Also partial unrolling / failures within nested calls is painful
         - Task Rejuvenation: If something going wrong just kill it and have another process do the work -> Masks failure. Controversial.
         	- Martin Renard's Group (MIT): Solution is that anytime you might read from bad data / e.g. segfault -> just return random data and stuff works!-> no one noticed the corruption (in the case of web apps).
            - Micro-reboot Idea (Stanford - Candea / Armando Fox).
            

Q: Is DRAM always next to core on board?


# 2016-Sept-9 - Lecture 2 
Paper: Implementing Remote Procedure Calls Birrell 1984
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
