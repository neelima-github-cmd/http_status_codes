# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 13:54:07 2020

@author: Neelima Sunku
"""

#Binary search
#Iterative binary search

def binary_search_iterative(numberslist, value):
    low = 0
    high = len(numberslist)-1
    while(low <= high):
        mid = (low + high)//2
        if numberslist[mid] > value : high = mid-1
        elif numberslist[mid] < value : low = mid+1
        else :return mid
    return -1

A = [534, 246,933,127,277,321,454,565,220]
print(binary_search_iterative(A,277))