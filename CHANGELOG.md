# Changelog
All notable changes to the "swarmlib" pypi package will be documented in this file.  
This project follows [semantic versioning](https://semver.org/).

## 2019-01-24 - v0.6.1
* **Changed** cuckoo search: Ensure each nest is assigned a cuckoo position in the update step

## 2019-01-24 - v0.6.0
* **Changed** the visualization of the _firefly algorithm_ and the _cuckoo search_. Now they both include velocities.
* **Changed** the firefly algorithm including its API. Now it replays the same problem if `--continuous` is set.
* **Changed** the `--continuous` flag. It requires no parameter anymore.
* **Changed** the `--two-opt` flag. It requires no parameter anymore.

## 2020-01-22 - v0.5.0
* **Added** a feature that performs _particle swarm optimization_ for one of the provided 2D functions. After each step the intermediate solution is plotted.
* **Changed** the API. Now the classes `*Problem` can be directly imported from the `swarmlib` module.

## 2020-01-19 - v0.4.1
* **Changed** pypi tags to enhance the package's discoverability.

## 2020-01-19 - v0.4.0
* **Added** a feature that enables the _cuckoo search_ for one of the provided 2D functions. After each step the intermediate solution is plotted.

## 2020-01-09 - v0.3.2
* **Fixed** a bug in the firefly algorithm that caused the application to crash when the ackley function was selected.

## 2019-10-30 - v0.3.1
* **Fixed** a bug in the ACO algorithm that chose the next node by its maximal attractiveness. Now the next node is chosen randomly weighted by its attractiveness

## 2018-12-18 - v0.3.0
* **Added** command line option `--continuous` for the firefly algorithm to indicate, whether the algorithm should run continuously or not
* **Added** logging for the current best and overall best intensity found of the firefly algorithm

## 2018-12-14 - v0.2.0
* **Added** a feature that enables the _firefly algorithm_ for one of the provided 2D functions. After each step the intermediate solution is plotted.

## 2018-11-29 - v0.1.0
* **Added** a feature that performs [2-opt](https://en.wikipedia.org/wiki/2-opt) search once on each partial solution after each iteration. It can be disabled via the argument `--two-opt false`.
* **Fixed** an import bug that caused the application to crash instantly

## 2018-11-23 - v0.0.1
* **Initial Release**
* **Added** a feature that enables solving the Traveling Salesman Problem using the _Ant Colony Optimization_ approach and plots the result afterwards
