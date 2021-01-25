from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

# https://github.com/pybind/python_example/
ext_modules = [
    Pybind11Extension(
        "_pyfma",
        # Sort input source files to ensure bit-for-bit reproducible builds
        # (https://github.com/pybind/python_example/pull/53)
        ["src/pybind11.cpp"],
    )
]

if __name__ == "__main__":
    setup(
        cmdclass={"build_ext": build_ext},
        ext_modules=ext_modules,
        zip_safe=False,
    )
