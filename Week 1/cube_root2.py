#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 15:10:02 2019

@author: aleksandar
"""

cube = 28
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of",cube,'is',guess)