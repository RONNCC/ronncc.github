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

# 2016-Oct-14

Dynamo Paper

- Eventual Consistency -> Vector Clocks (Bayou) / Red Blue  Consistency  
- Consistent Hashing / Chord
- Gossip Protocols
- SLOs & 99.9% Percentile Latency
- Merkle Trees

# 2016-Sept-30

The Design and Implementation of a Log-Structured File System

How many disks are at $x -> estimate data per second ingestion / disk storage  
- Context Raid: (IBM / Disk Size)
- Balance
- Spindles vs $/tb vs trut?
	- RAID Levels
- Reliability / MTTR / MTBF / MTTF etc.
- Schroeder
- RAID6 vs Cross-rack/de
- Section Remapping is eww (inserts seeks into reads). 


## Reliability
- Raid vs Tape Storage vs zone replication (buddy data centers!) 
- http://firstround.com/review/the-three-infrastructure-mistakes-your-company-must-not-make/
- Monitor everything
- https://en.wikipedia.org/wiki/Jerry_Saltzer has an undergrad book & class on relability eng

## RAID
- 0- striping, 1- mirror, 2- ecc, 3- single group, 4/5 sector. 
- https://community.netapp.com/fukiw75442/attachments/fukiw75442/data-ontap-discussions/2334/1/WAFL.pdf
- Hard drives are not as good as promised
- Failures correlated 
- MTTRs are increasing (fast + bigger disks)
- Failures increase (esp during heavy use!) 



"When you're operating at googlebooksoft scale" every server cannot be a special snowflake  

# 2016-Sept-26

Paper: AFS Howard 88

## AFS:
- \# of users > 5-10k
- Efficient servers by whole-file caching
- Server crash -> pause
- No Net? Maybe local cache if lease
- Typically 1 user prer file or read only
- Evaluation?:
	- Benchmark (Modified Andrew Benchmark)
    - Ran commmands - You can see amdahls law's and don't have interactions b/w file ops
    - Experience:
    	- Much slower than local
        - Better than 1 server
        - Killed Server

## Dropbox:
- 500M ~ users.
- work offline?
  - Conflict handling / merges
  - Human / Piss someone off

## Lustre, etc: / Panasas
- Storage: Sharded in Parallel - 10 Comps. Performance!!!
- GFS Looks similar -> pushed requirements to apps -> append semantics

## NFS
- More cluster-y
- Survive crashes
- Transparent
- Caching! -> Validate on use. (Block Based)
- Didn't have consistent access. 
- 3 second attr cache

## How does local ops do things?
- Read(fd ..) -> Get a file handle (vol, inode, gen \#) -> Make server stateless and idempotent. 

Q: How make generation \#?   
Q: Why is TCP Better > UDP For Services? Because Firewalls like TCP Better generally  

# 2016-Sept-23

Paper: Using Model Checking to Find Serious File System Errors Yang 04

- Fuzzing  is helpful
    - Link against ASAM (address sanitizer) / LibFuzz / AFL - American Fuzzy Lop
    - Industry "State of Art" / Adaptive Fuzzing

- Filesystems are ugly to fuzz
    - People test general not edge cases
	- Crash/Reboot => long
        - Sometimes true that disks do what you tell it - write [w1, fsync, w2] - you should have w1 if w2, ... - disks sometimes consistent - if you do certain things
        - Untested Code in Drivers: Error States 
   
- What do filesystems look like?
	- Well known superblock -> links to '/' directory or similar, 
   	- '/' then has names -> inodes with inodes pointing to blocks. Blocks can point to blocks. 
   	- Important Consistent Things
   		- If delete dog (file), you can just delete entry in directory. Bad issue is if name deleted but lost state about ops in file system. You have pointer gone but inodes/blocks are allocated. 
       	- How do we know if this happens? **FSCK**
        - What if we delete inodes, and then crash (dont delete name chunk)? We start overwriting other things
        if we try to write to it. 
        - When deleting you always delete & unlink then do unfree.
        - When you make a new file - first allocate & then link & then names and things.
        - If you do these in order you should have consistent. But large performance penalty for fsync. 
    - ext2 so fast vs BSD Fast File System, but loses data - last 30 sec sometimes - wrong order of ops can throw your FS away. 
    - JFS - Journaling FS. / ReiserFS also a thing
    - BTRFS is the new cool thing 
    - Checksums -> Stop instead of corruption failures
    
- Imagine building a soda dispenser

Coin -(Insert)-> Select State 
Select -Water-> Dispense
Select -Soda-> Select

What is correctness look like? 
- State always valid, you have to pay, you always get what you ask for

Back to Model Checking
- State Compaction (heuristic) e.g. ignore filenames
    - Hashbased comparisons
- Explore Efficiently
- Find Impl Bugs (vs Model Checking usually being correctness)
- It's hard to specify correctness (cool paper: SQCK: a declarative file system checker) 
- Fsck was the basis for their correctness?
- CMC + Stubs. They forwarded syscalls to their state machine 


SSDs - New FS's try to do large sequential writes, Disk drivers make Log Structured File Systems, optimize small things - "Turf War". (So they work with legacy FS). 

Disks not predictable - There's a paper by Eric Brewer.

Question: DSLs for specifying equality relations i.e. things that are the same in a filesystem?  
Question: Is disk control algorithms a research area still?
Question: No code gen for formal models? 



# 2016-Sept-12
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
