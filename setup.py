# -*- coding: utf-8 -*-
from cx_Freeze import setup, Executable

executables = [
    Executable('PyEVO_Set.py')
]

setup(name='PyEVO_Set',
      version='0.1',
      description='PyEVO_Set',
      executables=executables
      )
