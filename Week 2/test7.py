#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 13:28:37 2019

@author: aleksandar
"""

def factory(b):
    def newf(x):
        return (x * b)
    return newf

doubler = factory(2)
tripler = factory(3)
print("Result ", doubler(6), tripler(6))