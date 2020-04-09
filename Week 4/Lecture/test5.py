#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:31:14 2019

@author: aleksandar
"""

def get_ratios(L1, L2):
    """Assumes: L1 and L2 are lists of equal length of numbers
    Returns: a list containing L1[i]/L2[i] """

    ratios = []
    for ix in range(len(L1)):
        try:
            ratios.append(L1[ix]/float(L2[ix]))
        except ZeroDivisionError:
            ratios.append(float('NaN'))
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios
                
                