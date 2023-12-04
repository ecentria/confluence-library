from setuptools import setup, find_packages
from confluence import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='confluence_library',
    version=__version__,
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",

    url='https://gitlab.com/dwaskowski/py-bot-library.git',
    author='Dmitrij Waskowski',
    author_email='',

    packages=find_packages(exclude=[]),

    install_requires=[
        'atlassian-python-api',
    ],
)
