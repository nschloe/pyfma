# -*- coding: utf-8 -*-
#
import pyfma


def test_fma():
    out = pyfma.fma(3.0, 2.0, 1.0)
    assert out == 7.0
    return
