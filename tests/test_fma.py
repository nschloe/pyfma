import numpy

import pyfma


def test_fma():
    out = pyfma.fma(3.0, 2.0, 1.0)
    assert out == 7.0


def test_numpy():
    x = numpy.full((2, 3, 4), 3.0)
    y = numpy.full((2, 3, 4), 2.0)
    z = numpy.full((2, 3, 4), 1.0)
    out = pyfma.fma(x, y, z)
    assert out.shape == (2, 3, 4)
    assert numpy.all(out == 7.0)
