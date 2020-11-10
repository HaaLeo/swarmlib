# Changelog
All notable changes to the "swarmlib" pypi package will be documented in this file.  
This project follows [semantic versioning](https://semver.org/).

## Unreleased

## 2020-11-10 - v0.11.0
* **Added** visualization of the _alpha_, _beta_ and _delta_ wolves for the grey wolf optimizer ([#14](https://github.com/HaaLeo/swarmlib/issues/14)).
* **Added** top level `--seed` flag which allows to set the random bit generator's initial state for reproducible results.
* **Changed** the visualization. Now the initial as well as the end-position are shown unanimated as well.

## 2020-11-07 - v0.10.0
* **Added** [landscapes](https://github.com/nathanrooy/landscapes#readme) as a dependency to enable more benchmark functions ([#15](https://github.com/HaaLeo/swarmlib/issues/15)). Contributed by Alex F ([@alxfmpl](https://github.com/alxfmpl)). Thanks a lot 🚀.

## 2020-07-21 - v0.9.0
* **Added** _grey wolf optimizer_ ([#12](https://github.com/HaaLeo/swarmlib/issues/12)). Perform the grey wolf optimization algorithm on one of the selected 2D-functions. Contributed by Nimish Verma ([@NimishVerma](https://github.com/NimishVerma)) and greatly appreciated 🚀.

## 2020-04-13 - v0.8.1
* **Fixed** a bug that caused the ACO algorithm to fail. Due to other third party packages swarmlib now requires `matplotlib<3.2.0`.

## 2020-04-07 - v0.8.0
* **Added** the _artificial bee colony_ algorithm. After each step the intermediate solution is plotted.

## 2020-02-17 - v0.7.0
* **Added** dark mode. It is enabled via the `--dark` flag.
* **Changed** `--continuous` and `--interval` flags. Both are now top level flags.
* **Changed** the API of the ant colony optimization.
* **Changed** the `tsp_file` argument to an option. Now `--tsp-file` is optional. By default the built-in burma14 problem is used.

## 2020-01-25 - v0.6.2
* **Changed** cuckoo search visualization: when a nest is abandoned / newly generated color its transition differently.
* **Fixed** cuckoo search visualization: now the abandon transition is mapped to the correct nest.

## 2020-01-24 - v0.6.1
* **Changed** cuckoo search: Ensure each nest is assigned a cuckoo position in the update step

## 2020-01-24 - v0.6.0
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
