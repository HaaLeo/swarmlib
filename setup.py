# ------------------------------------------------------------------------------------------------------
#  Copyright (c) Leo Hanisch. All rights reserved.
#  Licensed under the BSD 3-Clause License. See LICENSE.txt in the project root for license information.
# ------------------------------------------------------------------------------------------------------

from os import path

from setuptools import find_packages, setup

# pylint: disable=exec-used,undefined-variable

with open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), 'r', encoding='utf8') as rf:
    LONG_DESCRIPTION = rf.read()

with open(path.join(path.abspath(path.dirname(__file__)), 'swarmlib/_version.py'), 'r', encoding='utf8') as f:
    exec(f.read())

setup(
    name='swarmlib',  # PEP8: Packages should also have short, all-lowercase names, the use of underscores is discouraged
    version=__version__,
    packages=find_packages(exclude=['*test']),
    # Include files specified in MANIFEST.in
    include_package_data=True,
    description='Implementation and visualization of different swarm optimization algorithms.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Leo Hanisch',
    license='BSD 3-Clause License',
    install_requires=[
        'landscapes==0.0.10',
        'tsplib95>=0.7.1, <1.0.0',
        'matplotlib>=3.3.2, <4.0.0',
        'networkx>=2.5, <3.0',
        'numpy>=1.19.3, <2.0.0'
    ],
    project_urls={
        'Documentation': 'https://github.com/HaaLeo/swarmlib/wiki',
        'Source': 'https://github.com/HaaLeo/swarmlib',
        'Issue Tracker': 'https://github.com/HaaLeo/swarmlib/issues',
        'Changelog': 'https://github.com/HaaLeo/swarmlib/blob/master/CHANGELOG.md#changelog',
        'Funding': 'https://github.com/sponsors/HaaLeo',
        'gitter.im': 'https://gitter.im/HaaLeo/swarmlib'
    },
    python_requires='>=3.6',
    keywords=[
        'swarm',
        'swarmlib',
        'lib',
        'library',
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
        'algorithm',
        'cuckoo',
        'cuckoos',
        'search',
        'levy',
        'flights',
        'particle',
        'particles',
        'pso',
        'PSO',
        'artificial',
        'bee',
        'bees',
        'colony',
        'ABC',
        'abc',
        'heuristic',
        'grey',
        'wolf',
        'optimizer',
        'gwo',
        'GWO'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    entry_points={
        'console_scripts': [
            'swarm=swarmlib.__main__:run_swarm'
        ]
    }
)
