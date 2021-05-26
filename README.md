# pyfma

[Fused multiply-add](https://en.wikipedia.org/wiki/Multiply%E2%80%93accumulate_operation#Fused_multiply%E2%80%93add)
for Python.

[![PyPi Version](https://img.shields.io/pypi/v/pyfma.svg?style=flat-square)](https://pypi.org/project/pyfma)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/pyfma.svg?style=flat-square)](https://pypi.org/pypi/pyfma/)
[![GitHub stars](https://img.shields.io/github/stars/nschloe/pyfma.svg?style=flat-square&logo=github&label=Stars&logoColor=white)](https://github.com/nschloe/pyfma)
[![PyPi downloads](https://img.shields.io/pypi/dm/pyfma.svg?style=flat-square)](https://pypistats.org/packages/pyfma)

[![Discord](https://img.shields.io/static/v1?logo=discord&label=chat&message=on%20discord&color=7289da&style=flat-square)](https://discord.gg/hnTJ5MRX2Y)

[![gh-actions](https://img.shields.io/github/workflow/status/nschloe/pyfma/ci?style=flat-square)](https://github.com/nschloe/pyfma/actions?query=workflow%3Aci)
[![codecov](https://img.shields.io/codecov/c/github/nschloe/pyfma.svg?style=flat-square)](https://codecov.io/gh/nschloe/pyfma)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

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
tox
```

### License
pyfma is published under the [MIT license](https://en.wikipedia.org/wiki/MIT_License).
