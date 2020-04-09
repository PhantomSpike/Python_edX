#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 11:42:39 2019

@author: aleksandar
"""

try:
    a = int(input('Tell me one number:'))
    b = int(input('Tell me another number:'))
    print('a/b = ', a/b)
    print('a + b = ', a+b)
except ValueError:
    print('Could not convert to number.')
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print('Something went very wrong.')
        