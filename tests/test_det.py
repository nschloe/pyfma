import numpy as np

import pyfma


# See <https://www.johndcook.com/blog/2020/05/31/kahan-determinant/>
def test_determinant():
    a = np.pi
    b = np.exp(1.0)
    c = 355 / 113
    d = 23225 / 8544
    naive = a * d - b * c

    ref = -7.039440876218302263286205e-7
    assert abs(naive - ref) < 1.0e-13

    w = b * c
    e = pyfma.fma(-b, c, w)
    f = pyfma.fma(a, d, -w)
    kahan = f + e

    ref = -7.039440876218302263286205e-7
    assert abs(kahan - ref) < 1.0e-13
