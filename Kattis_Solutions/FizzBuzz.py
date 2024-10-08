x, y, n = map(int, input().split())

i = 0
for i in range(1, n + 1):
    if i % x == 0 and i % y == 0:
        print('FizzBuzz')
    elif i % y == 0:
        print('Buzz')
    elif i % x == 0:
        print('Fizz')
    else:
        print(i)
