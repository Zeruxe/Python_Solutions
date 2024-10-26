def count_pairs(n, m):
    count = 0
    for a in range(int(n**0.5) + 1):
        b = n - a**2
        if b >= 0 and a + b**2 == m:
            count += 1
    return count

n, m = map(int, input().split())

print(count_pairs(n, m))