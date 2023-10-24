from setuptools import setup, find_packages
import os
import shutil
import subprocess
from distutils.cmd import Command


class DistCommand(Command):

    description = "build the distribution packages (in the 'dist' folder)"
    user_options = []

    def initialize_options(self): pass
    def finalize_options(self): pass

    def run(self):
        if os.path.exists('build'):
            shutil.rmtree('build')
        subprocess.run(["python", "setup.py", "sdist", "bdist_wheel"])

class TestCommand(Command):

    description = "run all tests with pytest"
    user_options = []

    def initialize_options(self): pass
    def finalize_options(self): pass

    def run(self):
        import pytest
        test_dir = 'test'  # Adjust this path to the location of your test directory
        return pytest.main([test_dir])
        

setup(
    name="Benz",
    version="1.0.0",
    packages=find_packages("src"),
    install_requires=["numpy"],
    tests_require=['pytest', 'pytest-cov'],
    setup_requires=['wheel'],
    cmdclass={
    'dist': DistCommand,
    'test': TestCommand,
    },
    python_requires='>=3.7',
)
