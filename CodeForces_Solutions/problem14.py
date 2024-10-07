k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

counter = 0

for i in range(1, d + 1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        counter += 1

print(counter)


#k = int(input())
#l = int(input())
#m = int(input())
#n = int(input())
#d = int(input())

#list = []
#given_list = []
#counter = 0

#if k == 1 or l == 1 or m == 1 or n == 1:
#    print(d)
#else:
#    for i in range(n):
#        list.append(k)
#        list.append(l)
#        list.append(m)
#       list.append(n)
#        break

#print(list)
#for j in range(1, d+1):
#    given_list.append(j)


#for t in range(len(given_list)):
#    if list[t] == given_list[t]:
#        counter += 1
#        given_list.remove(given_list[t])
#    else:
#        list = [x * 2 for x in list]


#print(given_list) #- 1-24
#print(list) #- 1-4
#print(d-counter)
#- 1 2 3 4 

#- 2 4 6 8

#- 4 8 12 16

#- 5 16 24 32

#, Test case 2 below---------

#- 2 3 4 5 

#- 4 6 8 10

#- 8 12 16 20

#- 16 24 32 40