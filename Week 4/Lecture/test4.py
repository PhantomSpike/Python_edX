#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 12:50:16 2019

@author: aleksandar
"""

data = []
file_name = input('Provide a name of a file of data: ')

try:
    fh = open(file_name,'r')
except IOError:
    print('cannot open',file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')
            data.append(addIt)

finally:
    fh.close()
    
gradesData = []
if data:
    for student in data:
        try:
            name = student[0:-1]
            grades = int(student[-1])
            gradesData.append([name,[grades]])
        except ValueError:
            gradesData.append([student[:],[]])
            
                
            
        