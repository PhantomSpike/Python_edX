#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 00:12:02 2019

@author: aleksandar
"""

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = string.ascii_lowercase
    stringy = list(set(alphabet) - set(lettersGuessed))
    stringy.sort()
    return ''.join(stringy)
    


print(getAvailableLetters(lettersGuessed))