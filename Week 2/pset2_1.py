#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 19:14:09 2019

@author: aleksandar
"""
      # Test Case 1:
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
          
for month in range(0,12):
    min_p = monthlyPaymentRate*balance
    balance =  balance - min_p
    int_b = (annualInterestRate/12)*balance
    balance = balance + int_b
    #print('Month ' + str(month) + ' Remaining balance: ' + str(balance))
    
print('Remaining balance: ' + str(round(balance,2)))
    