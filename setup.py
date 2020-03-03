import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tutorterminal-matheusgr",
    version="0.0.1",
    author="Matheus Gaudencio",
    author_email="matheusgr@gmail.com",
    description="A small example package",  # TODO
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheusgr/tutorterimanl",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
