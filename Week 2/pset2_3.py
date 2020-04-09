#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 20:34:05 2019

@author: aleksandar
"""

balance = 999999
annualInterestRate = 0.18
int_m = annualInterestRate/12
low_p = balance/12.0
high_p = (balance*((1 + int_m)**12))/12.0
balance_n = 1
epsilon = 0.009
n = 0
fp = (low_p + high_p)/2

while abs(balance_n) > epsilon:
    balance_n = balance
    #n += 1
    for month in range(0,12):
        balance_n =  balance_n - fp
        int_b = int_m *balance_n
        balance_n  = balance_n + int_b
    if balance_n < 0:
        high_p = fp
    else:
        low_p = fp
        
    fp = (low_p + high_p)/2
    #print('Trial #' + str(n) + ': Lower bound ' + str(low_p) + ' Upper bound ' + str(high_p))
    #print('Balance: ' + str(balance_n))
    
print('Lowest Payment: ' + str(round(fp,2)))