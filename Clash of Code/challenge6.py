# Print
# a
# vertical
# banner
# with 3 columns.
#
# You
# will
# be
# given
# one
# line
# of
# input
# which
# contains
# the
# message
# to
# be
# printed
# on
# the
# banner.
#
# The
# left
# column
# contains
# the
# input
# text
# from top to
#
# bottom.
# The
# middle
# column
# must
# be
# filled
# with space characters.
# The
# right
# column
# contains
# the
# input
# text
# from bottom to
#
# top.
# Input
# Line
# 1: message
# A
# line
# of
# text, to
# be
# printed
# on
# the
# banner
# Output
# N
# lines: The
# banner
# Constraints
# The
# input
# text
# will
# not exceed
# 100
# characters in length.
# Example
# Input
# Hello
# World
# Output
# H
# d
# e
# l
# l
# r
# l
# o
# o
# W
#
# W
# o
# o
# l
# r
# l
# l
# e
# d
# H
#

m = input()
for i, j in zip(m, m[::-1]):print(i, j)