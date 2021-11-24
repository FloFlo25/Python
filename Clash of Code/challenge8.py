# You need to simplify the fraction
# The numerator is the top number in a fraction and the denominator is the one bellow the line.
#
# If you don't know how to simplify a fraction, this is how you do it with a example:
# If numerator is 4 and denominator is 6 the you can figure out that the greatest common factor between them is 2. With that information, You can figure out that the fraction is (4/2)/(6/2) and you should output 2/3.
# Input
# Line 1: An integer numerator
# Line 2: An integer denominator
# Output
# The simplified fraction
# Constraints
# 1 ≤ numerator < 9^9
# numerator ≤ denominator ≤ 9^9
# Example
# Input
# 4
# 6
# Output
# 2/3

import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
d = int(input())
gcd = math.gcd(n, d)
print(f"{int(n/gcd)}/{int(d/gcd)}")
