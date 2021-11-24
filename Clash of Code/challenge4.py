# Each programming language has its own conventions.
# Your company has just switched from one language that uses snake_case to one using camelCase.
# Your boss has tasked you with converting variable names from snake_case to camelCase.
#
# To do this, strip the variable name of all underscores (_) and capitalize the letter after each underscore.
# Input
# A single line containing the variableName in snake_case.
# Output
# A single line with the variableName converted to camelCase.
# Constraints
# The variableName will always be in valid snake_case. It will never be a CONSTANT or contain any uppercase letters.
# It can, however, contain numbers.
# Example
# Input
# test_case
# Output
# testCase
v=input().split('_')
print(v[0]+''.join([i.capitalize() for i in v[1:]]))


