n = int(input())  
x = input().strip()  

black_groups = []
black_count = 0

for i in range(n):
    if x[i] == 'B':
        black_count += 1 
    else:
        if black_count > 0:
            black_groups.append(black_count) 
            black_count = 0  

if black_count > 0:
    black_groups.append(black_count)

print(len(black_groups))
if black_groups:
    print(" ".join(map(str, black_groups)))
