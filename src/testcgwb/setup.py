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
     read('docs', 'CHANGES.rst')]
)

classifiers = [
    "Framework :: Plone",
    "Framework :: Plone :: 4.0",
    "Framework :: Plone :: 4.1",
    "Framework :: Plone :: 4.2",
    "Framework :: Plone :: 4.3",
    "Programming Language :: Python",
    "Topic :: Software Development"]

name = 'testcgwb'
setup(
    name=name,
    namespace_packages=[
    ],
    version=version,
    description='Project %s',
    long_description=long_description,
    classifiers=classifiers,
    keywords='',
    author='kiorky <kiorky@localhost>',
    author_email='kiorky@localhost',
    url='http://www.generic.com',
    license='GPL',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'setuptools',
        'z3c.autoinclude',
        'Plone',
        'chardet',
        'plone.app.upgrade',
        # with_ploneproduct_pacaching
        'plone.app.caching',
        # with_ploneproduct_dexterity
        'collective.dexteritytextindexer',
        'plone.app.dexterity',
        'plone.app.referenceablebehavior',
        'plone.directives.dexterity',
        'plone.directives.form',
        # with_ploneproduct_patheming
        'plone.app.theming',
        'plone.app.themingplugins',
        # with_binding_pil
        'Pillow',
        # -*- Extra requirements: -*-
    ],
    extras_require={
        'test': ['plone.app.testing', 'ipython']
    },
    entry_points={
        'z3c.autoinclude.plugin': ['target = plone'],
    },
)
# vim:set ft=python:
