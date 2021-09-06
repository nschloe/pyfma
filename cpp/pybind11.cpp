#include <cmath>

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

double fma_wrap(double x, double y, double z) {
  return fma(x, y, z);
}

float fmaf_wrap(float x, float y, float z) {
  return fmaf(x, y, z);
}

long double fmal_wrap(long double x, long double y, long double z) {
  return fmal(x, y, z);
}

PYBIND11_MODULE(_pyfma, m) {
  m.def("fma", py::vectorize(fma_wrap));
  m.def("fmaf", py::vectorize(fmaf_wrap));
  m.def("fmal", py::vectorize(fmal_wrap));
}
