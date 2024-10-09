n = int(input())
sequence = list(input())

list = []

if len(sequence) == 2:
    if sequence[0] == '4' and sequence[1] == '4':
        print("YES")
        exit()
    elif sequence[0] == '7' and sequence[1] == '7':
        print("YES")
        exit()
    else:
        print("NO")
        exit()
else:
    length_of_sequence = n/2
    for i in range(n):
        if sequence[i] == '4' or sequence[i] == '7':
            list.append(sequence[i])
            
        else:
            print("NO")
            exit()
    
first_half = list[:len(list)//2]
second_half = list[len(list)//2:]

cnt_first_half = 0
cnt_second_half = 0

for i in range(len(first_half)):
    cnt_first_half += int(first_half[i])

for i in range(len(second_half)):
    cnt_second_half += int(second_half[i])

if cnt_first_half == cnt_second_half:
    print("YES")
else:
    print("NO")
