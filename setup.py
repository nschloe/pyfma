from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup

# https://github.com/pybind/python_example/
ext_modules = [
    Pybind11Extension(
        "_pyfma",
        ["cpp/pybind11.cpp"],
    )
]

if __name__ == "__main__":
    setup(
        cmdclass={"build_ext": build_ext},
        ext_modules=ext_modules,
        zip_safe=False,
    )
