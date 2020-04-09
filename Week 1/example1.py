#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 22:26:13 2019

@author: aleksandar
"""

x = float(input("Enter a number for x:"));
y = float(input("Enter a number for y:"));

if x ==y:
    print("x and y are equal")
    if y != 0:
        print("Therefore x/y is",x/y)
elif x<y:
    print("x is smaller");
else:
    print("y is smaller");