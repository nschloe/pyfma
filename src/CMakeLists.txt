FIND_PACKAGE(pybind11 REQUIRED)

FILE(GLOB pyfma_SRCS "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")

pybind11_add_module(pyfma ${pyfma_SRCS})
