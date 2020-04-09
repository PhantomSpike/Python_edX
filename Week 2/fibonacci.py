#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:08:59 2019

@author: aleksandar
"""

def fib(x):
     if x == 0 or x == 1:
         return 1
     else:
         return fib(x-1) + fib(x-2)