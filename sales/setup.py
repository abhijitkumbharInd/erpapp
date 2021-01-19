# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in sales/__init__.py
from sales import __version__ as version

setup(
	name='sales',
	version=version,
	description='To describe workflow of sales.',
	author='sd',
	author_email='sayali.d@indictranstech.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
