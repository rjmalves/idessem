from setuptools import setup, find_packages  # type: ignore
from idessem import __version__

long_description = ""
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = []
with open("requirements.txt", "r") as fh:
    requirements = fh.readlines()

setup(
    name="idessem",
    version=__version__,
    author="Rogerio Alves, Mariana Noel",
    author_email="rogerioalves.ee@gmail.com",
    description="Interface para arquivos do DESSEM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rjmalves/idessem",
    packages=find_packages(),
    package_data={"idessem": ["py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)
