# Changelog
All notable changes to the "swarmlib" pypi package will be documented in this file.  
This project follows [semantic versioning](https://semver.org/).

## 2018-11-29 - v0.1.0
* **Added** a feature that performs [2-opt](https://en.wikipedia.org/wiki/2-opt) search once on each partial solution after each iteration. It can be disabled via the argument `--two-opt false`.
* **Fixed** an import bug that caused the application to crash instantly

## 2018-11-23 - v0.0.1
* **Initial Release**
* **Added** a feature that enables solving the Traveling Salesman Problem using the Ant Colony Optimization approach and plots the result afterwards
