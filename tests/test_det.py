import numpy as np

import pyfma


# See <https://www.johndcook.com/blog/2020/05/31/kahan-determinant/>
def test_determinant():
    a = np.pi
    b = np.e
    c = 355 / 113
    d = 23225 / 8544
    naive = a * d - b * c

    # This dot-product is hard to compute, cf.
    # ```
    # accupy.cond([np.pi, np.e], [23225 / 8544, -355 / 113])
    # ```
    # ```
    # 48525073.17687677
    # ```
    # When computing all values a,b,c,d with many digits,  mpmath and wolframalpha both
    # give the same result
    # ```
    # mp.fdot([mp.pi, mp.e], [mp.mpf("23225 / 8544"), -mp.mpf("355 / 113")])
    # https://www.wolframalpha.com/input/?i=det%28%5B%5Bpi%2C+e%5D%2C+%5B+355+%2F+113%2C+23225+%2F+8544%5D%5D%29
    # ```
    # ```
    # -7.0394408762183022632862048647535951845717763186391e-7
    # -7.039440876218302263286204864753595184571776388044517499102e-7
    # ```
    # When starting with the np/Python rounding of a,b,c,d, accupy and mpmath give the
    # same result:
    # ```
    # mp.fdot([np.pi, np.e], [23225 / 8544, -355 / 113])
    # accupy.fdot([np.pi, np.e], [23225 / 8544, -355 / 113]).item()
    # ```
    # ```
    # [-7.0394408]801519439901320097075016572198321233241348743e-7
    # [-7.0394408]80151944e-07
    # ```
    # (The brackets mark the correct digits.)
    # The naive computation gives
    # ```
    # -7.039440870215685e-07
    # ```
    # which actually isn't much further from the real value either.
    ref = -7.0394408762183022632862048647535951845717763186391e-7
    print("naive:", naive, naive - ref)
    assert abs(naive - ref) < 1.0e-8 * abs(ref)

    w = b * c
    e = pyfma.fma(-b, c, w)
    f = pyfma.fma(a, d, -w)
    kahan = f + e
    print("kahan:", kahan, kahan - ref)

    assert abs(kahan - ref) < 1.0e-9 * abs(ref)
