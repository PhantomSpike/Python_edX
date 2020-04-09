#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 18:36:03 2019

@author: aleksandar
"""

an_letters = 'aefhilmnorsxAEFHILMNORSX'
word = input('I will cheer for you! enter a word: ')
times = int(input("Enthusiasm level [1-10]: "))
i = 0

while i < len(word):
    char = word[i]
    if char in an_letters:
        print("Give me an " + char + "! " + char)
    else:
        print("Give me a " + char + "! " + char)
    i+=1
print("What does that spell?")

for i in range(times):
    print(word,"!!!")