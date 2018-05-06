#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
import re
from collections import OrderedDict
from setuptools import setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

with io.open('flask_session_imp/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)


setup(
    name='Flask-Session-Imp',
    version='0.0.1',
    url='https://github.com/mikezone/flask-session',
    project_urls=OrderedDict((
        ('Documentation', 'https://github.com/mikezone/flask-session'),
        ('Code', 'https://github.com/mikezone/flask-session'),
        ('Issue tracker', 'https://github.com/pallets/flask/issues'),
    )),
    license='BSD',
    author='mike_chang',
    author_email='82643885@qq.com',
    maintainer='galaxy.Inc',
    maintainer_email='xxxx@galaxy.com',
    description='Adds server-side session support to your Flask application',
    long_description=readme,
    packages=['flask_session_imp'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    # python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
    install_requires=[
        'Flask>=0.8'
    ],
    test_suite='test_session',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
