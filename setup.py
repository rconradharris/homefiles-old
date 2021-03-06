from setuptools import setup, find_packages
from setuptools.command.sdist import sdist

name = 'homefiles'
version = '0.1.2'

setup(
    name=name,
    version=version,
    description='home directory files in git',
    url='https://github.com/rconradharris/homefiles',
    license='MIT',
    author='Rick Harris',
    author_email='rconradharris@gmail.com',
    packages=find_packages(exclude=['tests', 'bin']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6'
    ],
    install_requires=[], # removed for better compat
    scripts=['bin/homefiles'])
