def xo(s):
    if s.lower().count('x')==s.lower().count('o'):
        return True
    elif s.lower().count('x')==s.lower().count('o')==0:
        return True
    return False

print(xo('xo'))
print(xo('xoo'))
print(xo('zpzgsf'))
