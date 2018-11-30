# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from os import path

from setuptools import find_packages, setup

#pylint: disable=exec-used,undefined-variable

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), 'r') as rf:
    LONG_DESCRIPTION = rf.read()

with open(path.join(path.abspath(path.dirname(__file__)), 'swarmlib/_version.py'), 'r') as f:
    exec(f.read())

setup(
    name='swarmlib',  # PEP8: Packages should also have short, all-lowercase names, the use of underscores is discouraged
    version=__version__,
    packages=find_packages(exclude=['*test']),
    description='Implementation and visualization of different swarm optimization algorithms.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/HaaLeo/swarmlib',
    author='Leo Hanisch',
    license='BSD 3-Clause License',
    install_requires=[
        'tsplib95>=0.3.2, <1.0.0',
        'matplotlib>=3.0.2, <4.0.0',
        'networkx==2.1',  # Required by tsplib95 0.3.2
        'numpy>=1.15.4, <2.0.0'
    ],
    project_urls={
        'Issue Tracker': 'https://github.com/HaaLeo/swarmlib/issues',
        'Changelog': 'https://github.com/HaaLeo/swarmlib/blob/master/CHANGELOG.md'
    },
    python_requires='>=3.6',
    keywords=[
        'swarm',
        'swarmlib',
        'ant',
        'colony',
        'optimization',
        'optimisation',
        'traveling',
        'salesman',
        'problem',
        'TSP',
        'tsp',
        'ACO',
        'aco',
        'TSPLIB95',
        'tsplib95'
        'networkx',
        'visualization',
        'matplotlib',
        'firefly',
        'fireflies',
        'algorithm'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    entry_points={
        'console_scripts': [
            'swarm=swarmlib.main:run_swarm'
        ]
    }
)
