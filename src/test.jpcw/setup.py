import os

from setuptools import setup, find_packages

version = "1.0dev"


def read(*rnames):
    return open(
        os.path.join(".", *rnames)
    ).read()


long_description = "\n\n".join(
    [read("README.rst"),
     read("docs", "INSTALL.rst"),
     read("docs", "CHANGES.rst")]
)

classifiers = [
    "Framework :: Plone",
    "Framework :: Plone :: 4.0",
    "Framework :: Plone :: 4.1",
    "Framework :: Plone :: 4.2",
    "Framework :: Plone :: 4.3",
    "Programming Language :: Python",
    "Topic :: Software Development"]

name = "test.jpcw"
setup(
    name=name,
    namespace_packages=[
         "test"
    ],
    version=version,
    description="Project testcgwb",
    long_description=long_description,
    classifiers=classifiers,
    keywords="",
    author="kiorky <kiorky@localhost>",
    author_email="kiorky@localhost",
    url="http://www.generic.com",
    license="GPL",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "setuptools",
        "z3c.autoinclude",
        "Plone",
        "chardet",
        "plone.app.upgrade",
        "plone.app.themingplugins",
        "collective.dexteritytextindexer",
        "plone.app.dexterity [relations]",
        "plone.app.referenceablebehavior",
        "plone.directives.dexterity",
        "plone.directives.form",
        "plone.app.theming",
        "plone.app.themingplugins",
        # with_ploneproduct_galleria
        "collective.galleria",
        # with_ploneproduct_eeadaviz
        "eea.daviz[full]",
        "eea.relations",
        # with_binding_pil
        "Pillow",
        # with_ploneproduct_cpembed
        "collective.portlet.embed",
        # with_ploneproduct_cgallery
        "collective.gallery",
        # with_ploneproduct_configviews
        "collective.configviews",
        # with_ploneproduct_oembed
        "collective.oembed",
        "collective.portlet.oembed",
        # with_ploneproduct_pacaching
        "plone.app.caching",
        # with_ploneproduct_eeatags
        "eea.tags",
        # with_ploneproduct_plomino
        "Products.CMFPlomino",
        # -*- Extra requirements: -*-
    ],
    extras_require={
        "test": ["plone.app.testing", "ipython"]
    },
    entry_points={
        "z3c.autoinclude.plugin": ["target = plone"],
    },
)
# vim:set ft=python:
