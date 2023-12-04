from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='confluence_library',
    version="1.0.4",
    description='',
    long_description=long_description,
    long_description_content_type="text/markdown",

    url='https://github.com/ecentria/confluence-library.git',
    author='Dmitrij Waskowski',
    author_email='',

    packages=find_packages(where='src'),

    install_requires=[
        'atlassian-python-api=3.41.3',
    ],
)
