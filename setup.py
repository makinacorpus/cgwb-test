import os
from setuptools import setup, find_packages

version = "1.0dev"


def read(*rnames):
    return open(
        os.path.join('.', *rnames)
    ).read()

long_description = "\n\n".join(
    [read('README.rst'),
     read('docs', 'INSTALL.rst'),
     read('docs', 'HISTORY.rst')]
)

classifiers = [
    "Programming Language :: Python",
    "Topic :: Software Development"]
EPS = {
    'console_scripts': [
        'testcgwb = tata.toto.testcgwb.testcgwb:main',
    ]
 }
name = 'tata.toto.testcgwb'
setup(
    name=name,
    namespace_packages=[
         'tata',
    ],
    version=version,
    description='Project %s',
    long_description=long_description,
    classifiers=classifiers,
    keywords='',
    author='ubuntu <ubuntu@localhost>',
    author_email='ubuntu@localhost',
    url='http://foo.net',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    extras_require={
        'test': ['plone.testing']
    },
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    # define there your console scripts
    entry_points=EPS,
)
# vim:set ft=python:
