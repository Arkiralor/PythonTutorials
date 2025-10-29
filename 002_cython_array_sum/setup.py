from setuptools import setup
from Cython.Build import cythonize

# setup(
#     ext_modules=cythonize("sum_list_cython.pyx", language_level="3"),
# )

from setuptools import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize([
        Extension(name="matrix_multiply", sources=["matrix_multiply.pyx"])
    ], compiler_directives={"language_level": "3"})
)
