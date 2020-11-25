# How To Contribute

First of all, thank you for considering to contribute! :pray::tada:

The following is a set of guidelines for contributing to the [`swarmlib`](https://github.com/HaaLeo/swarmlib#readme). These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Table of Contents
[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Suggesting Enhancements](#suggesting-enhancements)
  * [Code Contribution](#code-contribution)
  * [Functions](#functions)
  * [Pull Requests](#pull-requests)
  * [Documentation](#documentation)

## How Can I Contribute?

### Reporting Bugs

To report a :bug: please file an issue using the [bug template](https://github.com/HaaLeo/swarmlib/issues/new?template=bug_report.md).
Please fill out the template tediously and provide information as detailed as possible.
Include screenshots or GIFs to visualize the problem.

### Suggesting Enhancements

To suggest an enhancement please file an issue using the [feature request template](https://github.com/HaaLeo/swarmlib/issues/new?template=feature_request.md).
Please fill out the template tediously and provide information as detailed as possible. 
The template will ask you for all relevant information.

### Code Contribution

Before starting to code please ensure you explicitly address an [issue](https://github.com/HaaLeo/swarmlib/issues) and comment on that issue indicating that you are working on it.

It would be a shame to reject a PR with your awesome work just because somebody else was faster or due to the lack of an issue.

#### Setup

First you need to fork the repo, clone it and install all dependencies.
I recommend you using a virtual environment for development.

```zsh
# Clone the repository
git@github.com:yourUserName/swarmlib.git

# Create virtual environment
python3 -m venv swarmlib/.venv
source swarmlib/.venv/bin/activate

# Install dependencies
pip3 install -r swarmlib/requirements-dev.txt

# Open the project with VS Code
code swarmlib
```

When you open the project the first time with VS Code the editor will ask you to install all recommended workspace extensions.
Confirm that dialog and you are all set up.

If you are new to VS Code and python check out the [official documentation](https://code.visualstudio.com/docs/python/python-tutorial) to get started.

#### Contribute a New Algorithm

If you want to contribute a new optimization algorithm ensure you opened an [issue](https://github.com/HaaLeo/swarmlib/issues/new?template=feature_request.md) beforehand.

##### Overview
Please reuse common components that can be found in the [`swarmlib/util`](https://github.com/HaaLeo/swarmlib/tree/master/swarmlib/util) directory.
There is no need to write a new visualization all over again :wink:.

When contributing a new algorithm you probably set up / change the following files:

```
swarmlib
    |- swarmlib
    |    |- your_awesome_new_algorithm
    |    |    |- __init__.py
    |    |    |- main.py                       // Provide the argument parser for the algorithm
    |    |    |- problem.py                    // Implement the algorithm here similar to PSO etc. Main work will be done here.
    |    |    |- animal.py                     // Optional: Subclass of coordinate.py to add additional functions if needed
    |    |    |- visualizer.py                 // Optional: Subclass of base_visualizer.py if any additional functions are needed
    |    |- __init__.py                        // import problem for easier API access
    |    |- __main__.py                        // Register the argument parser for the algorithm
    |    |- _version.py                        // Update the version according to semantic versioning
    |- tests
    |    |- your_awesome_new_algorithm_test    // Unit-Test the major components of your algorithm here (like the WOA does).
    |         |- ...
    |- setup.py                                // Add new keywords for the new algorithm
    |- README.md                               // Extend readme with a brief introduction of the algorithm
    |- CHANGELOG.md                            // Briefly state all relevant changes that will shipped with the next release
```

To get started, I recommend you to take a look at the implementation of the CS, PSO, ABC algorithms.

##### Programming notes

:heavy_exclamation_mark: avoid sorting the coordinates list.
This will cause the visualizer to wrongly replay position transitions.

Consider the following example with two particles:

The first particle _p1_ has coordinates `(0, 0)` and a value of `-1`.
The second particle _p2_ has coordinates `(1, 1)` and a value of `0`.
At the start of the algorithm we pass those positions to the visualizer:

Now lets apply an algorithm which causes the first particle _p1_ to update its position to `(-1, -1)` with value `-0.5`.
_p2_ now has a position `(2, 2)` with value `-2`.
Now if we sort the particles with respect to their value _p2_ is before _p1_. 
When we now pass those to the visualizer and calculated the velocities afterwards the visualizer will calculate wrong velocities:
* _p2_'s first position and _p2_'s second position
* _p1_'s first position and _p2_'s second position

```python
### Step 0
# p1 with position (0, 0) and value 0
# p2 with position (1, 1) and value -1
particles = [p1, p2]
positions = [particles.position for particle in particles]

visualizer = BaseVisualizer(**kwargs)
visualizer.add_data(positions=positions)

# Algorithm is applied...

### Step 2
# p1 with position (-1, -1) and value -0.5
# p2 with position (2, 2) and value -2
particles.sort() # this leads to [p2, p1]
positions = [particles.position for particle in particles]
visualizer.add_data(positions=positions)

# Now the visualizer has internal positions of 
# [
#   [(0, 0), (1, 1)], # Step 0
#   [(2, 2), (-1, -1)] # Step 1
# ]
# If now the velocities are calculated afterwards the visualizer calculates the velocities
# of (0, 0) -> (2, 2) and (1, 1) -> (-1, -1) which is obviously false
visualizer.replay()
```
### Functions

As of release _v0.10.0_ swarmlib uses the functions supplied by [landscapes](https://github.com/nathanrooy/landscapes#readme).
If you are missing a benchmark function please open an issue in the landscapes repository. 
Once the function is implemented there we are happy to update swarmlib's landscapes dependency.

### Pull Requests

Please follow these steps to have your contribution considered:

1. Reference the issue you are working on e.g.: `Fixes #1`
1. Add information on how you solved the issue.
1. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing.

After your pull request was submitted and the status checks pass I will review your changes.
I may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

### Documentation

Swarmlib organizes its documentation in a [wiki](https://github.com/HaaLeo/swarmlib/wiki).
Please ensure you opened an issue beforehand which provides an explanation of the changes you want to propose to the wiki.
After that you can fork the wiki and [submit a pull request](#pull-requests) to address that issue.
