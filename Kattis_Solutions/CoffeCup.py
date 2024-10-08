n = int(input())

k = list(input())

cnt = 0
coffe = 0

for i in range(n):
    if k[i] == '1':
        cnt += 1
        coffe = 2
    if k[i] == '0':
        if coffe > 0:
            cnt += 1
            coffe -= 1

print(cnt)