import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jupyter_dygraphs",
    version="0.0.2",
    author="Frank Dressel",
    description="simplifying dygraph graphs for jupyter",
    url="https://github.com/frankdressel/jupyter_dygraphs",
    packages=setuptools.find_packages(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
