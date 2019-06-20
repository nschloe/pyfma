# -*- coding: utf-8 -*-
#
# https://github.com/pybind/pybind11/issues/1004
from _pyfma import fma

from .__about__ import (
    __author__,
    __author_email__,
    __copyright__,
    __license__,
    __status__,
    __version__,
)

__all__ = [
    "__author__",
    "__author_email__",
    "__copyright__",
    "__license__",
    "__status__",
    "__version__",
    #
    "fma",
]