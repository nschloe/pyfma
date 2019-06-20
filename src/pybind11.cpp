#include <cmath>

#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
namespace py = pybind11;


double fma_wrap(double x, double y, double z) {
  return fma(x, y, z);
}

PYBIND11_MODULE(_pyfma, m) {
  m.def("fma", py::vectorize(fma_wrap));
}
