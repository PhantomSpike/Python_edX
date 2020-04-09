#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:44:53 2019

@author: aleksandar
"""


while True:
    try:
        n = input('Please enter an integer: ')
        n = int(n)
        break
    except ValueError:
        print('Input not an integer; try again')
print('Correct input of an integer!')