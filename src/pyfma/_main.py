import _pyfma
import numpy as np
from numpy.typing import ArrayLike


def fma(a: ArrayLike, b: ArrayLike, c: ArrayLike) -> np.ndarray:
    a = np.asarray(a)
    b = np.asarray(b)
    c = np.asarray(c)
    dtype = np.find_common_type([], [a.dtype, b.dtype, c.dtype])
    a = a.astype(dtype)
    b = b.astype(dtype)
    c = c.astype(dtype)

    if dtype == np.single:
        return _pyfma.fmaf(a, b, c)
    elif dtype == np.double:
        return _pyfma.fma(a, b, c)

    assert dtype == np.longdouble
    return _pyfma.fmal(a, b, c)
