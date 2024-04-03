strng = ' a #b\nc\nd $e f g'
markers = ['#','$']

a = ''
# str = strng.split('\n')
str = [' a #b', 'c', 'd $e f g']
# i = 0
# while i < len(str):
#     ii = 0
#     line = str[i]
#     while ii < len(line):
#         # subline = 
#         yes = any(a in line[ii] for a in markers)
#         while yes == False:
#             a += line[ii]
#             break
#         else:
#             break
#     i += 1
# print(a)

str = strng.split('\n')

# str = [' a #b',
#        'c',
#        'd $e f g']
a = ''
i = 0
tmp = []
while i < len(str):
    line = str[i]
    ii = 0
    x = ''
    while ii < len(line):
        letter = line[ii]
        yes = any(a in letter for a in markers)
        if yes:
            break
        else:
            # tmp.append(letter)
            x += letter
            ii += 1
    tmp.append(x)
    i += 1
a += '\n'.join(i.rstrip(' ') for i in tmp)
print(a)