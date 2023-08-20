from setuptools import setup, find_packages

setup(
    name="cannonical_assessment_package",
    version="1.0.0",
    author="Connor McGoey",
    description="Command line tool to download and parse debian packages",
    packages=find_packages(),
    install_requires=["typer"]
)
