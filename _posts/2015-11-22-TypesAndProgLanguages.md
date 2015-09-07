---
layout: post
title: Types and Programming Language Book Notes
category: ["Books"]
---


#Types and Programming Language Notes
By Benjamin Pierce @ Penn

#1
##1.1 Types in CS
- Formal methods vs Lightweight Formal Methods
	- E.g. Hoare Logic vs Model Checkers
	- 

> A type system is a tractable syntactic method for proving the absence of
certain program behaviors by classifying phrases according to the kinds
of values they compute
> ...
> A type system can be regarded
as calculating a kind of static approximation to the run-time behaviors of the
terms in a program. (Moreover, the types assigned to terms are generally calculated
compositionally, with the type of an expression depending only on
the types of its subexpressions.)

- Type systems are conservative and can prove some behaviors don't exist, not that they do.
##1.2 Why Type Systems?
 - Detecting Errors
 - 