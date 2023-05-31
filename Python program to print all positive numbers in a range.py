# -*- coding: utf-8 -*-
"""
Created on Wed May 31 12:15:00 2023

@author: 30112020
"""

# Python program to print positive Numbers in a List

# list of numbers
list1 = [12, -7, 5, 64, -14]
num = 0

# using while loop	
while(num < len(list1)):
	
	# checking condition
	if list1[num] >= 0:
		print(list1[num], end = " ")
	
	# increment num
	num += 1
	
