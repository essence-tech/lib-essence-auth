#!/usr/bin/env python

import sys

from distutils.core import setup

print sys.executable

setup(
    name='Essence Auth',
    version='2.0.4',
    description='Library for the Essence authentication service.',
    author='Josh Fyne',
    author_email='josh.fyne@essencedigital.com',
    url='https://github.com/essence-tech/lib-essence-auth',
    packages=['essenceauth', 'google.api'],
    install_requires=['grpcio', 'protobuf'],
    )
