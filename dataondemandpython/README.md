# On Demand Data in Python

A tutorial in four parts, by [Uche Ogbuji](http://uche.ogbuji.net)

## [Part 1: Python Iterators and Generators](https://www.ibm.com/developerworks/analytics/library/ba-on-demand-data-python-2)

**Learn how to process data in Python efficiently, on demand rather than pre-emptively**

For the longest time the standard way to process data in [Python](https://www.python.org/) was by building up data in lists, dictionaries and other such data structures. Many Python developers learn such techniques, and though in many cases they work well, they cause major problems when dealing with large quantities os data. It's easy to find the code running painfully slowly, or even running out of memory with such static data structures. Generators and iterators are techniques that have been around in Python for a while, and can help alleviate such problems.

## [Part 2: The magic of itertools](https://www.ibm.com/developerworks/analytics/library/ba-on-demand-data-python-2)

**Find a versatile toolkit for working with iterators in the standard library**

Python's motto has always been "Batteries included", to highlight its extensive standard library. Regardless there are many well-kept secrets among the standard modules, including itertools, which is less well known in part because iterators and generators are less well known. They are an essential part of the toolkit for workig woth these.

Published on June 22, 2018

## [Part 3: Coroutines and asyncio](https://www.ibm.com/developerworks/analytics/library/ba-on-demand-data-python-3)

**Learn how to dramatically improve the performance of software with input/output processing**

Much of the data in modern big data applications comes from the web or databases. You need to write code to process this at scale, but you don't want everything to grind to a halt in the process. Python 3 introduced a system for cooperative multitasking, which alleviates this problem, using asynchronous coroutines. Asynchronous coroutines build on similar concepts to generators. They are objects created from special functions which can be suspended and resumed. They make it possible to break down complex and inefficient processing into simple tasks that cooperate to maximize trade-offs between CPU and input/output. Learn these core techniques following a simple sequence of examples.


# Resources

* [awesome-asyncio](https://github.com/timofurrer/awesome-asyncio), "curated list of awesome Python asyncio frameworks, libraries, software and resources"
  * Does not include:
  * [Guillotina](https://guillotina.readthedocs.io/en/latest/), "Python AsyncIO REST Resource Application Server designed for high-performance, horizontally scaling solutions." (Uche hasn't tried this)
* [Used to be a list of 3rd party asyncio libraries & other notes that got archived with the entire repository](https://github.com/python/asyncio/wiki/ThirdParty)
