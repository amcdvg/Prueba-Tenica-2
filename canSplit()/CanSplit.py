# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 08:16:18 2021

@author: Alex
"""


# Partition the list into two sublists with the same sum
def canSplit(A):
 
    # calculate the sum of all list elements
    total_sum = sum(A)
 
    # variable to maintain the sum of processed elements
    sum_so_far = 0
 
    # do for each element in the list
    for i in range(len(A)):
 
        # if the sum of `A[0…i-1]` is equal to `A[i, n-1]`
        if sum_so_far == total_sum - sum_so_far:
            
            return 1
 
        # update `sum_so_far` by including the value of the current element
        sum_so_far += A[i]
       
 
    return 0
 
 
