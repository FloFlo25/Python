def unique_in_order(iterable):
    rezult = []
    prev = None
    for char in iterable[0:]:
        if char!=prev:
            rezult.append(char)
            prev=char

    return rezult

print(unique_in_order([1,2,2,4,5,6,7,7]))
print(unique_in_order(["Marius","Darius","Marcel","Marius","Marius"]))

