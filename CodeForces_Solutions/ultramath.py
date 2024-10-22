n = list(map(int, input().strip()))
m = list(map(int, input().strip()))

list_output = []

for i in range(len(n)):
    if n[i] != m[i]:
        list_output.append('1')
    else:
        list_output.append('0')
        
print(''.join(list_output))