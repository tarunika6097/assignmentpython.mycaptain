# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:20:03 2023

@author: 30112020
"""

abc= input('Please enter a string ')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print (most_frequent(abc))
