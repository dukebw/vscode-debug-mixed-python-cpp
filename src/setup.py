from distutils.core import setup, Extension


setup(
    name="myadd",
    version="1.0.0",
    description="Python interface for the myadd C library function",
    author="Brendan",
    author_email="brendanw.duke@gmail.com",
    ext_modules=[Extension("myadd", ["myadd.cpp"])],
)
