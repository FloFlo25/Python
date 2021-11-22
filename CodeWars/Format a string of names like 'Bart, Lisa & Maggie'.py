# Given: an array containing hashes of names
#
# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
#
# Example:
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# # returns 'Bart, Lisa & Maggie'
#
# namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# # returns 'Bart & Lisa'
#
# namelist([ {'name': 'Bart'} ])
# # returns 'Bart'
#
# namelist([])
# # returns ''
def namelist(names):
    result = None
    for dic in names:
        if names.index(dic)<len(names)-2:
            print(list(dic.values())[0],end=', ')
        elif names.index(dic)>len(names)-2<len(names):
            print(' & '+list(dic.values())[0],end='')
        else:
            print(list(dic.values())[0],end='')

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
