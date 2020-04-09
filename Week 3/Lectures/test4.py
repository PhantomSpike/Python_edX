#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 17:23:45 2019

@author: aleksandar
"""

def remove_dup(L1,L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
            
def remove_dup_new(L1,L2):
    L1_copy = L1[:]
    for e in L1_copy:
        if e in L2:
            L1.remove(e)