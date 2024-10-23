n = list(map(str,input().strip()))

list = []

i = 0

while i < len(n):
    if n[i] == '-':
        if i + 1 < len(n) and n[i + 1] == '-':
            list.append('2')
            i += 2
        else:
            list.append('1')
            i += 2
    elif n[i] == '.':
        list.append('0')
        i += 1


print(''.join(list))   #print in normal format to the standard output
