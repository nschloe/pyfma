import _pyfma
import numpy as np
from numpy.typing import ArrayLike

p = np.promote_types

def fma(a: ArrayLike, b: ArrayLike, c: ArrayLike) -> np.ndarray:
    a = np.asarray(a)
    b = np.asarray(b)
    c = np.asarray(c)
    dtype = p(p(a.dtype, b.dtype), c.dtype)
    a = a.astype(dtype)
    b = b.astype(dtype)
    c = c.astype(dtype)

    if dtype == np.single:
        return _pyfma.fmaf(a, b, c)
    elif dtype == np.double:
        return _pyfma.fma(a, b, c)

    assert dtype == np.longdouble
    return _pyfma.fmal(a, b, c)
