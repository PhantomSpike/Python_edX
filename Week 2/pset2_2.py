#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 19:53:15 2019

@author: aleksandar
"""

balance = 3926
annualInterestRate = 0.2
int_m = annualInterestRate/12
fp = 0
balance_n = 1

while balance_n > 0:
    fp += 10
    balance_n = balance
    for month in range(0,12):
        balance_n =  balance_n - fp
        int_b = int_m *balance_n
        balance_n  = balance_n + int_b
    
print('Lowest Payment: ' + str(fp))
        
    

