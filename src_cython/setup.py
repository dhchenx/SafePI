import os
from distutils.core import setup, Extension
from Cython.Build import cythonize

setup(
    ext_modules=cythonize((
        Extension(
            name="Person",
            sources=["src/Person.py"],
            language="c",

        ),
    ),build_dir="build")
)

