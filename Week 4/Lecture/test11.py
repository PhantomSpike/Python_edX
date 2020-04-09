#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 22:47:43 2019

@author: aleksandar
"""

def avg(grades):
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)