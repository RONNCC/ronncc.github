---
layout: post
title: Types and Programming Language Book Notes
category: ["Books"]
---

Author & Citations to Benjamin Pierce @ Univ. of Pennsylvania

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
	 - Strength depends on expressiveness of typechecker
	 - e.g. You can do dimension analysis 
 - Abstraction
	 - Module Languages
	 - Documentation and clues about purpose of code
 - Language Safety
	 - "Safe Language is one that protects its own abstractions"