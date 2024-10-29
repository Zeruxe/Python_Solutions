n, d = map(int, input().split())

counter = 0
counter_max = 0

for i in range(d):
    x = input().strip()
    if '1' in x and not '0' in x:
        counter_max = max(counter, counter_max)
        counter = 0
    elif '0' in x:
        counter += 1
    
counter_max = max(counter, counter_max)

print(counter_max)	