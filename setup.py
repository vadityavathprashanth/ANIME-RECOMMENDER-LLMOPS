from setuptools import setup, find_packages

with open ("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name= "ANIME-RECOMMENDER",
    version= "1.0",
    author= " Prashanth Vadityavath",
    packages= find_packages(),
    install_requires= requirements,
)