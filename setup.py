#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Essence Auth',
    version='0.2',
    description='Library for Essence authentication',
    author='Josh Fyne',
    author_email='josh.fyne@essencedigital.com',
    url='https://github.com/essence-tech/lib-essence-auth',
    packages=['essenceauth',],
    install_requires=['requests'],
    )
