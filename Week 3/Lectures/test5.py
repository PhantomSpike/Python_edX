#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 09:15:32 2019

@author: aleksandar
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    count = 0
    for w in aDict:
        count += len(aDict[w])
    return count

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    if len(aDict.items())!=0:
        temp = {}
        for w in aDict:
            temp[w] = len(aDict[w])
            max_val = max(temp.values())
            final_list = []
        for k in temp:
            if temp[k] == max_val:
                final_list.append(k)
        return final_list[0]
    else:
        return None
