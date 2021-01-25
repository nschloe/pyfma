# pyfma

[Fused multiply-add](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation#Fused_multiply%E2%80%93add)
for Python.

[![CircleCI](https://img.shields.io/circleci/project/github/nschloe/pyfma/master.svg?style=flat-square)](https://circleci.com/gh/nschloe/pyfma/tree/master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![PyPi Version](https://img.shields.io/pypi/v/pyfma.svg?style=flat-square)](https://pypi.python.org/pypi/pyfma)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/pyfma.svg?logo=github&label=Stars&logoColor=white&style=flat-square)](https://github.com/nschloe/pyfma)

Fused multiply-add computes `(x*y) + z` with a _single rounding_. Useful for dot
products, matrix multiplications, polynomial evaluations (e.g., with Horner's rule),
Newton's method for evaluating functions, convolutions, artificial neural networks etc.

Use as
```python
import pyfma

out = pyfma.fma(3.0, 2.0, 1.0)  # 3.0*2.0 + 1.0 = 7.0
```
Also works with NumPy inputs:
```python
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
pip install pyfma
```
you can install/upgrade.

#### Manual installation

For manual installation (if you're a developer or just really keen on getting the
bleeding edge version of pyfma), there are two possibilities:

 * Get the sources, do `pip install .`. This does the trick most the time.
 * As a fallback, there's a CMake-based installation. Simply go `cmake
   /path/to/sources/` and `make`.

### Testing

To run the pyfma unit tests, check out this repository and type
```
pytest
```

### License
pyfma is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
