---
published: false
categories:
  - misc
  - Talks
---
# HTPS Keynote

## Before

- Storage has evolved
	- (from Direct, SAN, Storage clusters + REST API)
- Computing Evolved
	- Single proc -> Multi -> RPC -> SOA -> Microservices
- Computing Storage Use
	- Direct File I/O


## State

- Durable state + consistency (transactions/updates/message semantics)
- Session State - multi op transactions; sessions are hard @ microservices
- inside/outside data
	- outside data is immutable

### Careful Replacement
- disks can trash block during write: (old -> trash -> new)
- hardware fixes careful replacement issue
- transactions bundle + solve careful replacement
- workflows need careful transactional replacement now


## Read your writes?
- Strong consistently - (R after W):
	- Even as scales you can r after w
	- Sometime delay if sick/dead (releader election)

- Weakly consistent (not R after W):
	- No guarantee write update old replica - read old value
	- R/W consistent SLA - skip sick/dead servers

- Cached Data
	- KV pairs versioned, unsure if newest.

Different stores for diff uses!
Immutability can fix these - only one version to get.

## Stateful Sessions And Transactions

- Stateful sessions worked well for SOA: Distributed Transactions + Across Machines

## Transactions, Sessions, Microservice

- Requests flow to request routing.
- Session state needed for cross-request TV
- Microservice Transaction are typically 1 store request
- No cross request transactions

Theres no substitute for interchangibility
