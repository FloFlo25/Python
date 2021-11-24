# Count the occurrences of each character and output the product of said occurrences.
# ex(sample1): AABBCC
# A is 2, B is 2, C is 2, so answer is 8(=2*2*2).
# Input
# S is given in one line.
# S consists of alphanumeric characters.
# Output
# Output a single number of the product of them.
# Constraints
# 1 <= |S| <= 50
# Example
# Input
# AABBCC
# Output
# 8
import numpy as np
# from collections import Counter as ct
# s = input().lower()
# print(np.prod([i for i in ct(s.lower()).values()]))

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print("Sum of arrays:",(array1+array2)[0::])
#-------------------------------------------------------
# s=input()
# a=1
# for e in set(s):a*=s.count(e)
# print(a)