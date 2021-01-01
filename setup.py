
import os
from setuptools import setup

setup(
  name = "pybfms_mem_core",
  packages=['mem_bfms_core'],
  package_dir = {'' : 'src'},
  author = "Matthew Ballance",
  author_email = "matt.ballance@gmail.com",
  description = ("Provides core classes for use by memory-oriented BFMs"),
  license = "Apache 2.0",
  keywords = ["SystemVerilog", "Verilog", "RTL", "CocoTB"],
  url = "https://github.com/pybfms/pybfms_mem_core",
  setup_requires=[
    'setuptools_scm',
  ],
)

