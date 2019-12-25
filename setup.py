"""
To install locally:
    python setup.py install

To upload to PyPi:
    python setup.py sdist
    pip install twine
    twine upload dist/*
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MangaReaderScraperGUI",
    version="0.01",
    author="superDross",
    author_email="dross78375@gmail.com",
    description="Manga scraper GUI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/superDross/MangaReaderScraperGUI",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    entry_points={"console_scripts": ["manga-scraper-gui = scraper.__main__:gui"]},
    install_requires=["MangaReaderScraper==0.4", "PyQt5==5.13.2"],
)
