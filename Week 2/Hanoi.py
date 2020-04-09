#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:58:21 2019

@author: aleksandar
"""

def printMove(fr,to):
    print('move from ' + str(fr) + ' to ' + str(to))
    
def Towers(n,fr,to,spare):
    if n == 1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)