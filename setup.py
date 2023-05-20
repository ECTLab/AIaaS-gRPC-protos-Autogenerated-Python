#!/usr/bin/env python

from setuptools import setup, find_packages


requirements = [
]

with open('README.md') as f:
    readme = f.read()

setup(
    name='AIaaS_interface',
    author='AIaaS-Backend-Team',
    author_email='m.mahdi.m79@gmail.com',
    packages=find_packages(),
    license='Proprietary',
    description='Auto generate python codes of AIaaS gRPC interface. gRPCs available at: https://github.com/ECTLab/AIaaS-gRPC-protos',
    long_description=readme,
    install_requires=requirements,
    tests_require=requirements,
    keywords='AIaaS gRPC interface python',
    classifiers=[
        'Development Status :: 0 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
