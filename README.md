# pyfma

Fused multiply-add for Python.

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/pyfma/master.svg)](https://circleci.com/gh/nschloe/pyfma/tree/master)
[![PyPi Version](https://img.shields.io/pypi/v/pyfma.svg)](https://pypi.python.org/pypi/pyfma)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/pyfma.svg?style=social&label=Stars)](https://github.com/nschloe/pyfma)


### Installation

pyfma can be [installed from the Python Package
Index](https://pypi.python.org/pypi/pyfma/), so with
```
pip install -U pyfma
```
you can install/upgrade.

#### Manual installation

For manual installation (if you're a developer or just really keen on getting
the bleeding edge version of pyfma), there are two possibilities:

 * Get the sources, type `sudo python setup.py install`. This does the trick
   most the time.
 * As a fallback, there's a CMake-based installation. Simply go `cmake
   /path/to/sources/` and `make`.

### Testing

To run the pyfma unit tests, check out this repository and type
```
pytest
```

### Distribution

To create a new release

1. bump the `__version__` number (in `setup.py` _and_ `src/pyfma.i`)

2. publish to PyPi and GitHub:
    ```
    make publish
    ```

### License

pyfma is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
