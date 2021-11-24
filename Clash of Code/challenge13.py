# Given a time, output the angles of the two hands.
# Input
# Line 1: Time in hh:mm format.
# Output
# Line 1: Angle of Hour hand.
# Line 2: Angle of Minute hand.
# Constraints
# Time is given in 24-hour format.
# 0/12 o'clock is 0°.
# Example
# Input
# 00:00
# Output
# 0
# 0
import sys
import math
#00:15
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

hour,minute = input().split(':')
h=int(hour)%12
t=60*h+int(minute)
print(t/2 if t%2==0 else t/2.0)
print(int(minute)*6)
