import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tutorterminal",
    version="v0.2",
    scripts=["ttterminal"],
    author="Matheus Gaudencio",
    author_email="matheusgr@gmail.com",
    description="A tool to show terminal tutorials.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/matheusgr/tutorterminal",
    download_url='https://github.com/matheusgr/tutorterminal/tarball/master',
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "Topic :: System :: Shells",
        "Intended Audience :: Education",
    ],
    install_requires=[
      'ansimarkup',
    ],
    python_requires='>=3.2',
    test_suite='nose.collector',
    tests_require=['nose'],
)
