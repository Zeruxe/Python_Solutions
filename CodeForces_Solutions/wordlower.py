n = list(map(str,input().strip()))

lower_counter = 0
upper_counter = 0

list = []

for i in range(len(n)):
    if n[i].islower():
        lower_counter += 1
        list.append(n[i])
    else:
        upper_counter += 1
        list.append(n[i])


final = ''.join(list)

if lower_counter >= upper_counter:
    print(final.lower())
else:
    print(final.upper())
