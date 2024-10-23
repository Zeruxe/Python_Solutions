n = int(input())

inc = 0
m = 0

for i in range(0, 500):
    if m == n:
        print("YES")
        exit()
    inc += 1
    m += inc

print("NO")






#* 0,1,3,6,10,15,21,28