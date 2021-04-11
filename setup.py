import os

from setuptools import setup

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

current_dir = os.path.abspath(os.path.dirname(__file__))

about = {}
with open(os.path.join(current_dir, 'firebasepy', '__version__.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

packages = [
    'firebasepy',
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description='',
    long_description=readme,
    long_description_content_type='text/markdown',
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    install_requires=requirements,
    python_requires='>=3.7',
    license=about['__license__'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)