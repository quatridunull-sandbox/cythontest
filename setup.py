from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

# instantiate Cyton Extension object
ext = Extension(
    "example",                           # name of extension
    ["example.pyx", "Example.cpp"],  # filename of our Cython source
    language="c++",                      # this causes Cython to create C++ source
    include_dirs=["."]   ,                  # usual stuff
    libraries=["stdc++"],                # ditto
    extra_link_args=[],                  # if needed
    cmdclass = {'build_ext': build_ext}
    )

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [ext]
)

