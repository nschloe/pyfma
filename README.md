# pyfma

[Fused
multiply-add](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation#Fused_multiply%E2%80%93add)
for Python.

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/pyfma/master.svg)](https://circleci.com/gh/nschloe/pyfma/tree/master)
[![PyPi Version](https://img.shields.io/pypi/v/pyfma.svg)](https://pypi.python.org/pypi/pyfma)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/pyfma.svg?logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/pyfma)

Fused multiply-add computes `(x*y) + z` with a _single rounding_. Useful for dot
products, matrix multiplications, polynomial evaluations (e.g., with Horner's
rule), Newton's method for evaluating functions, convolutions, artificial
neural networks etc.

Use as
```
import pyfma

out = pyfma.fma(3.0, 2.0, 1.0)  # 3.0*2.0 + 1.0 = 7.0
```
Also works with NumPy inputs:
```
import numpy
import pyfma

x = numpy.random.rand(3, 4, 5)
y = numpy.random.rand(3, 4, 5)
z = numpy.random.rand(3, 4, 5)

out = pyfma.fma(x, y, z)
```

Built with [pybind11](https://github.com/pybind/pybind11).

> **Caution**
> The C/C++ implementation of FMA in *MS Windows* is [reportedly
> broken](https://bugs.python.org/msg312480). Use with care.

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

 * Get the sources, type `python3 setup.py install`. This does the trick
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
