n, d = map(int, input().split())

x = list(map(int, input().split()))

counter = 0

for i in range(len(x)):
    if x[i] <= d:
        counter += 1
    elif x[i] > d:
        counter += 2

print(counter)