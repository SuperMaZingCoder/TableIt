from setuptools import setup, find_packages

with open("README.md") as mdfile:
    long_description = mdfile.read()

with open("LICENSE.txt") as mdfile:
    lisence = mdfile.read()


setup(
    name = "TableIt",
    packages = ["TableIt"],
    version="0.0.0",
    description="",
    long_description = long_description,
    author = "SuperMaZingCoder",
    url = "https://github.com/SuperMaZingCoder/TableIt",
    keywords = ["tables"],

    license=lisence,

    classifiers=[
        "Development Status :: 6 - Mature",
        "Framework :: IDLE",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.0",
        "Topic :: Printing",
        
    ]
)