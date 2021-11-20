import string

def is_pangram(s: str):
    no_dubs = set(s.lower())
    return all(item in no_dubs for item in string.ascii_lowercase)

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))