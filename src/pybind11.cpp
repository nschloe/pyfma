#include <cmath>

#include <pybind11/pybind11.h>
namespace py = pybind11;


double fma_wrap(double x, double y, double z) {
  return fma(x, y, z);
}

PYBIND11_MODULE(pyfma, m) {
  m.def("fma", &fma_wrap, "Fused multiply-add");
}
