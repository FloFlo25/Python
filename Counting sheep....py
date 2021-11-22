def count_sheeps(sheeps):
    return len([sheep for sheep in sheeps if sheep == True])


print(count_sheeps([True, True, True, False,
                    True, True, True, True,
                    True, False, True, False,
                    True, False, False, True,
                    True, True, True, True,
                    False, False, True, True]))
