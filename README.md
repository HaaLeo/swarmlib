# Ant Colony Optimization &#8212; aco4tsp

[![Pypi](https://img.shields.io/pypi/v/aco4tsp.svg?style=flat-square)](https://pypi.python.org/pypi/aco4tsp) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/aco4tsp.svg?style=flat-square)](https://pypi.python.org/pypi/aco4tsp) [![Stars](https://img.shields.io/github/stars/HaaLeo/ant-colony-optimization.svg?label=Stars&logo=github&style=flat-square)](https://github.com/HaaLeo/ant-colony-optimization/stargazers)  
[![PyPI - License](https://img.shields.io/pypi/l/aco4tsp.svg?style=flat-square)](https://pypi.python.org/pypi/aco4tsp) 
[![Build Status](https://img.shields.io/travis/HaaLeo/ant-colony-optimization/master.svg?style=flat-square)](https://travis-ci.org/HaaLeo/ant-colony-optimization) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  
[![Donate](https://img.shields.io/badge/-Donate-blue.svg?logo=paypal&style=flat-square)](https://www.paypal.me/LeoHanisch)

## Description

This repository implements an ant colony optimization algorithm for the traveling salesman problem (TSP) like Marco Dorigo, Mauro Birattari, and Thomas Stuetzle introduced in the [IEEE Computational Intelligence Magazine](https://ieeexplore.ieee.org/document/4129846) in November 2006 (DOI: 10.1109/MCI.2006.329691).  
The implementation was part of the course [Natural computing for learning and optimisation](https://is.cuni.cz/studium/eng/predmety/index.php?do=predmet&kod=NPFL107) at Charles University Prague in winter 2018/2019.

## Features

Enables to apply the ant colony optimization algorithm to a TSP using a [TSPLIB95](https://www.iwr.uni-heidelberg.de/groups/comopt/software/TSPLIB95/index.html) file and plots the result.

![Sample](https://raw.githubusercontent.com/HaaLeo/ant-colony-optimization/master/doc/Sample.png)

The algorithm solves the TSP and plots the result all _n_ iterations.  
The nodes are plot according to their coordinates read from the TSPLIB95 file. The _widths_ of the edges indicate the _amount of pheromone_ that is associated with this edge. If an edge is _blue_, it is part of the _best found path_.

## Usage
First you have to clone the repository:
```
git clone git@github.com:HaaLeo/ant-colony-optimization.git
cd ant-colony-optimization
```

### Client

To use the command line interface you need to package and install the pip package:
```
python setup.py sdist
pip install dist/aco4tsp-0.0.1.tar.gz --upgrade
```

To print all available options:
```
aco4tsp --help
```

Example:
```
ac04tsp resources/burma14.tsp 14
```

### From Source
If you prefer to run it from source, run the following to print all available options:
```
python aco4tsp/main.py --help
```

Example:
```
python aco4tsp/main.py resources/burma14.tsp 14
```

## Contribution

If you found a bug or are missing a feature do not hesitate to [file an issue](https://github.com/HaaLeo/ant-colony-optimization/issues/new/choose).  
Pull Requests are welcome!

## Support
When you like this package make sure to [star the repo](https://github.com/HaaLeo/ant-colony-optimization/stargazers). I am always looking for new ideas and feedback.  
In addition, it is possible to [donate via paypal](https://www.paypal.me/LeoHanisch).
