from setuptools import setup, find_packages

setup(
    name="datapulse-ds-toolkit",
    version="1.0.0",
    description="A beginner-friendly reusable toolkit for common data science tasks",
    author="DataPulse Student Group",
    packages=find_packages(),
    install_requires=["pandas>=1.5", "matplotlib>=3.6"],
    python_requires=">=3.9",
)
