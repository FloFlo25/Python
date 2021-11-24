# You need to compute the sum of all even and odd positive Integers up to n (n included) separately.
# Input
# One integer n
# Output
# Line 1: sum_odd
# Line 2: sum_even
# Constraints
# 0<n<2^30
# 0<sum_*<2^40
# Example
# Input
# 1
# Output
# 1
# 0
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n=int(input())
o,e=0,0
for i in range(n+1):
    if i%2==0:e+=i
    else:o+=i
print(o)
print(e)
