---
categories:
  - Misc
comment: null
date: 2016-1-8
info: null
layout: post
published: true
sha: 3ffa8917ba5b3a74e6d875a14226aa8cd301690e
slug: the-post-5518
tags: []
title: Systems Design Notes
type: post
---

## Cloud
[- Try considering GCE over AWS for in-between region streaming, also significant time-to-first-byte difference and different long-term-cold-storage use cases ](http://blog.zachbjornson.com/2015/12/29/cloud-storage-performance.html)

## Distributed
- [Use epoll/kqueue not select/poll as they are more scalable](http://geocar.sdf1.org/fast-servers.html)
- CAP is kind of a lie [[1]](http://codahale.com/you-cant-sacrifice-partition-tolerance/#errata10221010) [[2]](https://voltdb.com/blog/clarifications-cap-theorem-and-data-related-errors)
- [Distributed Systems for New Entrants](https://www.somethingsimilar.com/2013/01/14/notes-on-distributed-systems-for-young-bloods/)

## App Architecture / Ops
- [The 12 Factor App](http://12factor.net/)
