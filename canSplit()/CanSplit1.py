# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 01:37:15 2021

@author: Alex
"""


# Partition the list into two sublists with the same sum
def canSplit(b):
 
    # do for each element in the list
    for i in range(len(b)):
        left_sum = 0
        for j in range(i):
            left_sum += b[j]
 
        right_sum = 0
        for j in range(i, len(b)):
            right_sum += b[j]
 
        # if the sum of `A[0…i-1]` is equal to `A[i, n-1]`
        if left_sum == right_sum:
            return 1
 
    # can´t be partitioned
    return 0
 
