# swarmlib

[![Pypi](https://img.shields.io/pypi/v/swarmlib.svg?style=flat-square)](https://pypi.python.org/pypi/swarmlib) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/swarmlib.svg?style=flat-square)](https://pypi.python.org/pypi/swarmlib) [![PyPI - Downloads](https://img.shields.io/pypi/dm/swarmlib.svg?style=flat-square)](https://pypistats.org/packages/swarmlib) [![Stars](https://img.shields.io/github/stars/HaaLeo/swarmlib.svg?label=Stars&logo=github&style=flat-square)](https://github.com/HaaLeo/swarmlib/stargazers)  
[![PyPI - License](https://img.shields.io/pypi/l/swarmlib.svg?style=flat-square)](https://pypi.python.org/pypi/swarmlib) 
[![Build Status](https://img.shields.io/travis/HaaLeo/swarmlib/master.svg?style=flat-square)](https://travis-ci.org/HaaLeo/swarmlib) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  
[![Donate](https://img.shields.io/badge/☕️-Buy%20Me%20a%20Coffee-blue.svg?&style=flat-square)](https://www.paypal.me/LeoHanisch/3eur)

## Description

This repository implements several optimization algorithms:
* [Ant Colony Optimization](#ant-colony-optimization)
* [Firefly Algorithm](#firefly-algorithm)
* [Cuckoo Search](#cuckoo-search)

## Installation

You can install the package with `pip` from [pypi](https://pypi.org/project/swarmlib):

```
pip3 install swarmlib

swarm --version
```

## Usage

To print all available algorithms:

```
swarm --help
```

## Ant Colony Optimization

This repository includes an ant colony optimization algorithm for the traveling salesman problem (TSP) like Marco Dorigo, Mauro Birattari, and Thomas Stuetzle introduced in the [IEEE Computational Intelligence Magazine](https://ieeexplore.ieee.org/document/4129846) in November 2006 (DOI: 10.1109/MCI.2006.329691).  
The implementation was part of the course [Natural computing for learning and optimisation](https://is.cuni.cz/studium/eng/predmety/index.php?do=predmet&kod=NPFL107) at Charles University Prague in winter 2018/2019.

### Features

Enables to apply the ant colony optimization algorithm to a TSP using a [TSPLIB95](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/) file and plots the result.

![ACO Sample](https://raw.githubusercontent.com/HaaLeo/swarmlib/master/doc/ACO_Sample.png)

The algorithm solves the TSP and plots the result all _n_ iterations.  
The nodes are plot according to their coordinates read from the TSPLIB95 file. The _widths_ of the edges indicate the _amount of pheromone_ that is associated with this edge. If an edge is _blue_, it is part of the _best found path_.

To print all available options execute:

```
swarm ants -h
```

### API

In addition to the client you can also use the API:

```python
from swarmlib.aco4tsp.aco_problem import ACOProblem

problem = ACOProblem('/path/to/my/tsp-file.tsp', 10)
if problem.solve():
    problem.show_result()
```

## Firefly Algorithm

This repository includes the _firefly algorithm_ like Xin-She Yang introduced in his paper [Firefly Algorithms for Multimodal Optimization](https://link.springer.com/chapter/10.1007%2F978-3-642-04944-6_14) in 2009 (DOI: 10.1007/978-3-642-04944-6_14).  
The implementation was part of the course [Natural computing for learning and optimisation](https://is.cuni.cz/studium/eng/predmety/index.php?do=predmet&kod=NPFL107) at Charles University Prague in winter 2018/2019.

### Features

Enables to apply the firefly algorithm to one of the provided 2D functions. The algorithm tries to find the global minimum of the selected function.  

Currently two functions can be selected:
* [ackley](https://www.sfu.ca/~ssurjano/ackley.html)
* [michalewicz](https://www.sfu.ca/~ssurjano/michal.html)

![firefly algorithm](https://raw.githubusercontent.com/HaaLeo/swarmlib/master/doc/fireflies.gif)

To print all available options execute:

```
swarm fireflies -h
```

### API

In addition to the client you can also use the API:

```python
from swarmlib.fireflyalgorithm.firefly_problem import FireflyProblem
from swarmlib.util.functions import FUNCTIONS

problem = FireflyProblem(FUNCTIONS['michalewicz'], 14)
problem.solve()
```

## Cuckoo search

This repository also implements the _cuckoo search_ that was introduced by Xin-She Yang and Suash Deb in their paper [Cuckoo Search via Lévy flights](https://ieeexplore.ieee.org/document/5393690) in 2009 (DOI: 10.1109/NABIC.2009.5393690).  

### Features

Enables to apply cuckoo search to one of the provided 2D functions. The algorithm tries to find the global minimum of the selected function.  

Currently two functions can be selected:
* [ackley](https://www.sfu.ca/~ssurjano/ackley.html)
* [michalewicz](https://www.sfu.ca/~ssurjano/michal.html)

![cukoo search](https://raw.githubusercontent.com/HaaLeo/swarmlib/master/doc/cuckoos.gif)

To print all available options execute:

```
swarm cuckoos -h
```

### API

In addition to the client you can also use the API:

```python
from swarmlib.cuckoosearch.cuckoo_problem import CuckooProblem
from swarmlib.util.functions import FUNCTIONS

problem = CuckooProblem(function=FUNCTIONS['michalewicz'], nests=14)
best_nest = problem.solve()
problem.replay()
```

## Contribution

If you found a bug or are missing a feature do not hesitate to [file an issue](https://github.com/HaaLeo/swarmlib/issues/new/choose).  
Pull Requests are welcome!

## Support
When you like this package make sure to [star the repository](https://github.com/HaaLeo/swarmlib/stargazers). I am always looking for new ideas and feedback.  
In addition, it is possible to [donate via paypal](https://www.paypal.me/LeoHanisch/3eur).
