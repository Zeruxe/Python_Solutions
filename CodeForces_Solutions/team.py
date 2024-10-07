n = int(input())

count = 0

for _ in range(n):
    guess = list(map(int, input().split()))
    if guess.count(1) >= 2:
        count += 1

print(count)