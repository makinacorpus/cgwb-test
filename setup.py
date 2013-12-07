#!/usr/bin/env python
# -*- coding: utf-8 -
from setuptools import setup, find_packages

name = 'testcgwb'
version = "1.0dev"


def read(*rnames):
    return open(
        os.path.join('.', *rnames)
    ).read()


long_description = "\n\n".join(
    [read('README.rst'),
     read('docs', 'INSTALL.rst'),
     read('docs', 'CHANGES.rst')]
)
EPS = {
    'paste.app_factory':  [
        'main=testcgwb:main',
    ],
    'console_scripts': [
        '%s=testcgwb.webserver:main' % name ,
    ],
}
setup(
    name=name,
    namespace_packages=[
    ],
    version=version,
    description='Project testcgwb',
    long_description = '' ,
    author='ubuntu <ubuntu@localhost>',
    author_email='ubuntu@localhost',
    license='GPL',
    keywords='',
    url='http://www.generic.com',
    install_requires=[
        'setuptools',
        "PIL",
        "lxml",
        "elementtree",
        "CherryPy",
        "cryptacular",
        "gunicorn",
        "iniparse",
        "Paste",
        "PasteDeploy",
        "Pastescript",
        "pyramid",
        "pyramid_chameleon",
        "pyramid_debugtoolbar",
        "pyramid_zcml",
        "repoze.tm2",
        "repoze.vhm",
        "waitress",
        "WebError",
        "WebOb",
        "zope.component",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    # Make setuptools include all data files under version control,
    # svn and CVS by default
    include_package_data=True,
    zip_safe=False,
    extras_require={'test': ['IPython', 'plone.testing']},
    entry_points = EPS,
)
