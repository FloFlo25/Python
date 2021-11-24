# 1. Slice the code into widths of width.
# 2. Convert each 0-padded slice to binary.
# 3. Replace 0 with space and 1 with the given character.
# 4. Finally print the result with a new line for each slice.
# Input
# Line 1: Integer width
# Line 2: String character
# Line 3: String code
# Output
# The image contained in the code
# Constraints
# 3 <= width <= 19
# Example
# Input
# 1
# 1
# 1357
# Output
# 1
# 11
# 1 1
# 111
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w = int(input())
c = input()
s = input()

for i in range(0,len(s),w):
    print(str(bin(int(s[i:i+w]))[2:]).replace('0',' ').replace('1',c))
