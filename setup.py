"""
Oauth jaccount python package configuration.

tc-imba <liuyh615@sjtu.edu.cn>
"""

from setuptools import setup

setup(
    name='jaccountproxy',
    version='0.1.0',
    packages=['jaccountproxy'],
    include_package_data=True,
    install_requires=[
        'flask',
        'cachelib'
    ],
    dependency_links=[
        'git+ssh://git@github.com/tc-imba/python-oauth-jaccount.git'
    ]
)
