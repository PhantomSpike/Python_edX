#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:29:38 2019

@author: aleksandar
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    ln = len(aStr)
    if ln == 0:
        return False
    elif ln == 1:
        if char == aStr:
            return True
        else: 
            return False
    else:
        m_ix = int((ln - 1)/2)
        if char == aStr[m_ix]:
            return True
        elif char < aStr[m_ix]:
            return isIn(char, aStr[0:m_ix])
        else:
            return isIn(char, aStr[m_ix+1:])
    
        