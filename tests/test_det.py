import numpy as np

import pyfma


# See <https://www.johndcook.com/blog/2020/05/31/kahan-determinant/>
def test_determinant():
    a = np.pi
    b = np.exp(1.0)
    c = 355 / 113
    d = 23225 / 8544
    naive = a * d - b * c

    # This dot-product is hard to compute, cf.
    # ```
    # accupy.cond([np.pi, np.exp(1)], [23225 / 8544, -355 / 113])
    # ```
    # ```
    # 48525073.17687677
    # ```
    # mpmath and accupy both give roughly the same result
    # ```
    # mp.fdot([mp.pi, mp.exp(1)], [23225 / 8544, -355 / 113])
    # accupy.fdot([mp.pi, mp.exp(1)], [23225 / 8544, -355 / 113])
    # ```
    # ```
    # mpf('-0.0000007039440881364642881854950494754700045595555781461170140566248554188871587381024144643360959030530452283')
    # -7.039440880151944e-07
    # ```
    # wolframalpha gives a different number:
    # https://www.wolframalpha.com/input/?i=det%28%5B%5Bpi%2C+e%5D%2C+%5B+355+%2F+113%2C+23225+%2F+8544%5D%5D%29
    #
    # [-7.0394408]76218302263286204864753595184571776388044517499102e-7
    #
    # The brackets mark the correct digits.
    ref = -7.039440880151944e-07
    print("naive:", naive, naive - ref)
    assert abs(naive - ref) < 1.0e-8 * abs(ref)

    w = b * c
    e = pyfma.fma(-b, c, w)
    f = pyfma.fma(a, d, -w)
    kahan = f + e
    print("kahan:", kahan, kahan - ref)

    assert abs(kahan - ref) < 1.0e-15 * abs(ref)
