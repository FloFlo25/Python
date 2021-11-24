# The game mode is REVERSE: You do not have access to the statement. You have to guess what to do by observing the following set of tests:
# 01 Test 1
# Input
# Expected output
# 3
# adgjmpswz
# behknqtx
# cfiloruy
# abcdefghijklmnopqrstuwxyz
# 02 Test 2
# Input
# Expected output
# 5
# AAA
# BB
# C
# DD
# EEE
# ABCDEABDEAE
# 03 Test 3
# Input
# Expected output
# 5
# H D
# EW!
# LO
# LR
# OL
# HELLO WORLD!
# 04 Test 4
# Input
# Expected output
# 5
# Gnas
# Rewp
# Esas
# Asi4
# T t
# GREATness awaitsps4


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
words = []
for i in range(n):
    word = input()
    words.append(word)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

string = ""

while len(words) >= 1:
    w = words[0]
    words = words[1:]
    l,w = w[0],w[1:]
    string += l

    if w != "":
        words.append(w)
print(string)