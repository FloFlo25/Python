# You have to find the sum of the first x powers of a number n starting from 0. You will find that this puzzle will be easier if you know the trick
# Input
# n: an integer
# x: an integer
# Output
# The sum of the first x powers of n.
# Constraints
# x>=1 and n>=1
# Example
# Input
# 2
# 5
# Output
# 31
import math

n = int(input())
x = int(input())

print(int(math.fsum([n**i for i in range(x)])))