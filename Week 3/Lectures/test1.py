#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 15:08:05 2019

@author: aleksandar
"""

def q_and_r(x,y):
    q = x//y
    r = x%y
    return(q,r)
    
(quot,reman) = q_and_r(4,5)