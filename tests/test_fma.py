import numpy as np
import pytest

import pyfma


def test_fma():
    out = pyfma.fma(3.0, 2.0, 1.0)
    assert out == 7.0


@pytest.mark.parametrize("dtype", [np.single, np.double, np.longdouble])
def test_numpy(dtype):
    print(dtype)
    x = np.full((2, 3, 4), 3.0, dtype=dtype)
    y = np.full((2, 3, 4), 2.0, dtype=dtype)
    z = np.full((2, 3, 4), 1.0, dtype=dtype)
    out = pyfma.fma(x, y, z)

    assert out.shape == (2, 3, 4)
    assert np.all(out == 7.0)
    print(dtype, out.dtype)
    assert out.dtype == dtype
