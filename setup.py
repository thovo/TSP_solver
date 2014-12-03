__author__ = 'thovo'
import os

from setuptools import setup, find_packages

setup(
    name='TSP',
    version='0.0.1',
    description='Implement the algorithms for TSP problem',
    packages=find_packages(exclude='test_scripts'),
    install_requires=['xlwt', 'prettytable', 'numpy', 'matplotlib'],
    url='https://github.com/thovo/aa_practice_project',
    license='GNU General Public License (GPL)',
    author='Tho VO,Ahmed Hassan,Omar Samir',
    author_email='Tho VO<votuongtho@gmail.com>;Omar Samir <omar.samir3000@gmail.com>;Ahmed Hassan <ahmed.adel.hassan@hotmail.com>',
    long_description='Use for our practice project in TSP problems',
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Conceptual',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
