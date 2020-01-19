# Changelog
All notable changes to the "swarmlib" pypi package will be documented in this file.  
This project follows [semantic versioning](https://semver.org/).

## 2020-01-19 - v0.4.1
* **Changed** pypi tags to enhance the package's discoverability.

## 2020-01-19 - v0.4.0
* **Added** a feature that a feature that enables the cuckoo search for one of the provided 2D functions. After each step the intermediate solution is plotted.

## 2020-01-09 - v0.3.2
* **Fixed** a bug in the firefly algorithm that caused the application to crash when the ackley function was selected.

## 2019-10-30 - v0.3.1
* **Fixed** a bug in the ACO algorithm that chose the next node by its maximal attractiveness. Now the next node is chosen randomly weighted by its attractiveness

## 2018-12-18 - v0.3.0
* **Added** command line option `--continuous` for the firefly algorithm to indicate, whether the algorithm should run continuously or not
* **Added** logging for the current best and overall best intensity found of the firefly algorithm

## 2018-12-14 - v0.2.0
* **Added** a feature that enables the firefly algorithm for one of the provided 2D functions. After each step the intermediate solution is plotted.

## 2018-11-29 - v0.1.0
* **Added** a feature that performs [2-opt](https://en.wikipedia.org/wiki/2-opt) search once on each partial solution after each iteration. It can be disabled via the argument `--two-opt false`.
* **Fixed** an import bug that caused the application to crash instantly

## 2018-11-23 - v0.0.1
* **Initial Release**
* **Added** a feature that enables solving the Traveling Salesman Problem using the Ant Colony Optimization approach and plots the result afterwards
