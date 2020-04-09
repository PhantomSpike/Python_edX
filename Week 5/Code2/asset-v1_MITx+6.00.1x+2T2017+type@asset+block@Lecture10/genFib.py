# -*- coding: utf-8 -*-
"""
Created on Thu May 19 08:44:36 2016

@author: ericgrimson
"""

def genFib():
    fibn_1 = 1 #fib(n-1)
    fibn_2 = 0 #fib(n-2)
    while True:
        # fib(n) = fib(n-1) + fib(n-2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next

def genPrimes():
    p = 2;
    keep = [2]
    yield p
    while True:
        p += 1
        if [n for n in keep if p%n != 0] == keep:
            keep.append(p)
            yield p

def genPrimes2():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
        
