
from distutils.core import setup
from setuptools import find_packages

setup(
    name='aco4tsp', # PEP8: Packages should also have short, all-lowercase names, the use of underscores is discouraged
    version='0.0.1',
    packages=find_packages(exclude=['*test']),
    author='Leo Hanisch',
    install_requires=[
        'tsplib95==0.3.2',
        'matplotlib==3.0.2',
        'networkx==2.1'
    ],
    entry_points={
        'console_scripts':[
            'aco4tsp=aco4tsp.main:main'
        ]
    }
)
