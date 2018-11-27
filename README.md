# swarmlib

[![Pypi](https://img.shields.io/pypi/v/swarmlib.svg?style=flat-square)](https://pypi.python.org/pypi/swarmlib) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/swarmlib.svg?style=flat-square)](https://pypi.python.org/pypi/swarmlib) [![Stars](https://img.shields.io/github/stars/HaaLeo/swarmlib.svg?label=Stars&logo=github&style=flat-square)](https://github.com/HaaLeo/swarmlib/stargazers)  
[![PyPI - License](https://img.shields.io/pypi/l/swarmlib.svg?style=flat-square)](https://pypi.python.org/pypi/swarmlib) 
[![Build Status](https://img.shields.io/travis/HaaLeo/swarmlib/master.svg?style=flat-square)](https://travis-ci.org/HaaLeo/swarmlib) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  
[![Donate](https://img.shields.io/badge/-Donate-blue.svg?logo=paypal&style=flat-square)](https://www.paypal.me/LeoHanisch)

## Description

This repository implements several optimization algorithms.

>Currently only the ant colony optimization is included.

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

Enables to apply the ant colony optimization algorithm to a TSP using a [TSPLIB95](https://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/index.html) file and plots the result.

![Sample](https://raw.githubusercontent.com/HaaLeo/swarmlib/master/doc/ACO_Sample.png)

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

This repository includes the firefly algorithm like Xin-She Yang introduced in his paper [Firefly Algorithms for Multimodal Optimization](https://link.springer.com/chapter/10.1007%2F978-3-642-04944-6_14) in 2009 (DOI: 10.1007/978-3-642-04944-6_14).  
The implementation was part of the course [Natural computing for learning and optimisation](https://is.cuni.cz/studium/eng/predmety/index.php?do=predmet&kod=NPFL107) at Charles University Prague in winter 2018/2019.

### Features

### API

## Contribution

If you found a bug or are missing a feature do not hesitate to [file an issue](https://github.com/HaaLeo/swarmlib/issues/new/choose).  
Pull Requests are welcome!

## Support
When you like this package make sure to [star the repository](https://github.com/HaaLeo/swarmlib/stargazers). I am always looking for new ideas and feedback.  
In addition, it is possible to [donate via paypal](https://www.paypal.me/LeoHanisch).
