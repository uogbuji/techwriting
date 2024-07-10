# Workshop: Iterators, generators, coroutines and asyncio

by [Uche Ogbuji](https://ucheog.carrd.co/) of [Oori Data](https://oori.dev/)

## Blurb

Python developers should learn effective use of the iterator protocol when crunching large datasets. The lineage of such techniques extends to Python 3’s asyncio, valuable in boosting network applications. This workshop progresses from a firm grounding in iterators through generators & asyncio.

## Description

Building from the humble for loop through Python's async facilities for efficient I/0. This workshop offers a deep explanation of the iterator protocol, building rich fundamentals students can use when crunching large datasets with high performance. It builds from these basics through generators, and eventually to asyncio, an essential tool for boosting network application performance.

## Abstract

When you work with data in Python perhaps you build up structures comprising lists, dictionaries, etc. This works well in many cases, but if you're not careful you can end up with major problems while dealing with large quantities of data. One of the biggest reasons Python gets a bad rap for performance is that its native data structures are very easy to learn and use, but don't always scale particularly well.

Learn about iterators, a basic language feature which is not well enough appreciated, but allows for code that builds up data incrementally, for better scalability. Learn the most convenient way to write your own iterator—special types of functions called generators. Then prepare to be amazed as your understanding of generators leads you to understand even more sophisticated features such as coroutines and asynchronous control flow.

These topics have often intimidated users, because they require a shift in thinking from most programming 101 approaches, and available documentation is often very complicated. It's a shame, because the underlying concepts can be grasped by any developer, if explained in the right way, and they open the way to a massive increase in developer effectiveness and productivity. More and more of the most advanced Python libraries and tools use async patterns; this tutorial will demystify the concept and prepare even less experienced developers for modern programming.

Note: this tutorial will be very heavy on simple code examples. There is a lot to cover but it will move pretty quickly. Key topics include:

What's really in a for loop?
Sequences, iterables, iterators, etc.
Built-in features of iterators
Generator functions
List comprehensions versus generator expressions
Local state in generator functions
Asynchronous processes and coroutines
Python's asyncio features
Asynchronous I/O in practice
Audience level: Novice
