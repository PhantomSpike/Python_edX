#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:32:34 2019

@author: aleksandar
"""
count = 0
while count<5:
    count += 1
    print(count)
    if count == 3:
        break
else:
    print('I am else')