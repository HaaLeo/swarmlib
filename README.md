# swarmlib

[![Pypi](https://img.shields.io/pypi/v/swarmlib.svg?style=flat-square)](https://pypi.python.org/pypi/swarmlib) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/swarmlib.svg?style=flat-square)](https://pypi.python.org/pypi/swarmlib) [![Pypi - Downloads](https://img.shields.io/badge/dynamic/json?style=flat-square&color=green&label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fswarmlib)](https://pepy.tech/project/swarmlib) [![Stars](https://img.shields.io/github/stars/HaaLeo/swarmlib.svg?label=stars&logo=github&style=flat-square)](https://github.com/HaaLeo/swarmlib/stargazers)  
[![PyPI - License](https://img.shields.io/pypi/l/swarmlib.svg?style=flat-square)](https://raw.githubusercontent.com/HaaLeo/swarmlib/master/LICENSE.txt) [![Lint, Test, Bundle and Deploy](https://img.shields.io/github/workflow/status/HaaLeo/swarmlib/Lint%2C%20Test%2C%20Bundle%20and%20Deploy?label=Lint%2C%20Test%2C%20Bundle%20and%20Deploy&style=flat-square)](https://github.com/HaaLeo/swarmlib/actions?query=workflow%3A%22Lint%2C+Test%2C+Bundle+and+Deploy%22) [![Codecov](https://img.shields.io/codecov/c/github/HaaLeo/swarmlib?style=flat-square)](https://codecov.io/github/HaaLeo/swarmlib)  
[![Chat on Gitter](https://img.shields.io/badge/-chat%20on%20gitter-753a88.svg?logo=gitter&style=flat-square&labelColor=grey)](https://gitter.im/HaaLeo/swarmlib) [![Donate](https://img.shields.io/badge/☕️-Buy%20Me%20a%20Coffee-blue.svg?&style=flat-square)](https://www.paypal.me/LeoHanisch/3eur) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  

<p align="middle">
  <img src="https://raw.githubusercontent.com/HaaLeo/swarmlib/master/doc/light_mode.png" width="49%" />
  <img src="https://raw.githubusercontent.com/HaaLeo/swarmlib/master/doc/dark_mode.png" width="49%" /> 
</p>

## Description

This repository implements several swarm optimization algorithms and visualizes their (intermediate) solutions.
To run the algorithms one can either use the CLI (recommended) or the API.

For a list of all available algorithms and their detailed description [checkout the wiki](https://github.com/HaaLeo/swarmlib/wiki).

## Installation

You can install the package with `pip` from [pypi](https://pypi.org/project/swarmlib).
Installing the library in a virtual environment is recommended:

```zsh
# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install the latest version of swarmlib
pip install --upgrade swarmlib

# Verify installation
swarm --version
```

## Usage

To print all available algorithms:

```
swarm --help
```

## Contribution

If you found a bug or are missing a feature do not hesitate to [file an issue](https://github.com/HaaLeo/swarmlib/issues/new/choose) or to ask questions on [gitter](https://gitter.im/HaaLeo/swarmlib).
For a more detailed guide checkout the [CONTRIBUTING.md](https://github.com/HaaLeo/swarmlib/blob/master/CONTRIBUTING.md#how-to-contribute) file.

Pull Requests are welcome!

## Wiki

Swarmlib's wiki includes all of the documentation and more details to each algorithm.
It can be found [here](https://github.com/HaaLeo/swarmlib/wiki).

## Support
When you like this package make sure to [star the repository](https://github.com/HaaLeo/swarmlib/stargazers).
I am always looking for new ideas and feedback.

In addition, it is possible to sponsor this project via [PayPal](https://www.paypal.me/LeoHanisch/3eur) or [GitHub sponsors](https://github.com/sponsors/HaaLeo).

## Example

![Particle Swarm Optimization](https://raw.githubusercontent.com/HaaLeo/swarmlib/master/doc/example.gif)
