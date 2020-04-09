#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:34:36 2019

@author: aleksandar
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        test_val = a
    else:
        test_val = b
    
    while test_val > 1:
        if a%test_val == 0 and b%test_val == 0:
            return test_val
        else:
            test_val -= 1
            
    return test_val
