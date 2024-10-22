import math

n, m = map(int, input().split())

counter = 0

for i in range(n):
    for j in range(m):
        counter += 1

print(math.floor(counter/2))
