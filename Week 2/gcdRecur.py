#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:48:32 2019

@author: aleksandar
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == 0:
        return b
    elif b == 0:
        return a
    
    if a > b:
        return gcdRecur(b,a%b)
    elif b > a:
        return gcdRecur(a,b%a)
    else:
        return a