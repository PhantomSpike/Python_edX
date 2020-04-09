#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:46:37 2019

@author: aleksandar
"""
low = 0
high = 100
print('Please think of a number between 0 and 100!')
ans = 'b'

while ans != 'c':
    guess = int((low+high)/2)
    print('Is you secret number ' + str(guess) + '?',end='')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess
    elif ans == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: ' + str(guess))
        