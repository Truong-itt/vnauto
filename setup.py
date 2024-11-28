from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

setup(
    name="vnauto",
    version="1.0.0",
    description="A Python library for Vietnamese text normalization and processing",
    long_description=open("README.md").read(),
    long_description_content_typlse="text/markdown",
    author="TruongItt",
    author_email="hoduytruong280220@gmail.com",
    url="https://github.com/Truong-itt/vnauto", 
    license="MIT", 
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True, 
    package_data={
        "vnauto": ["data/*"],
    },
    install_requires=parse_requirements("requirements.txt"),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
