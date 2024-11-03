# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 11:23:48 2024

@author: brand

Write a Python program that writes out a
table of the function sin(x) vs. x, where
x is tabulated between 0 and 2pi with a
thousand entries. Follow the basic Python
program structure, including a main program
function.

"""

import numpy as np
from astropy.table import Table
from astropy.io import ascii
from astropy.io import fits

def sin_table():
    x_values = np.linspace(0, 2 * np.pi, 1000)
    sin_values = np.sin(x_values)
    
    data = Table([x_values,sin_values],
                 names=['x','sin(x)'])
    ascii.write(data, 'sintable.txt',
                format='commented_header')
    data_in = ascii.read('sintable.txt')
    print(data_in)

def main():
    sin_table()
    
if __name__=="__main__":
    main()