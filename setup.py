from setuptools import setup, find_packages

setup(
    name="myproject",
    version="1.0.0",
    packages=find_packages("src"),
    install_requires=["wheel"],
    tests_require=["pytest"],
)
