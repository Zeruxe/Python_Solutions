import sys

n = int(input())

list_enter = []
list_exit = []
list_max_value = []

counter = 0
running_sum = 0
max_tram = float('-inf')


for i in range(n):
    exit,enter = map(int, input().split())
    list_enter.append(enter)
    list_exit.append(exit)

for j in range(len(list_enter)):
    if list_exit[j] == 0 and j == 0 and len(list_enter) == 1:
        counter = list_enter[j]
        list_max_value.append(counter)
        print(" ".join(map(str, list_max_value)))
        exit()
    else:
        counter = list_enter[j] - list_exit[j]
        list_max_value.append(counter)

for k in range(len(list_max_value)-1):
    running_sum = running_sum + list_max_value[k]
    max_tram = max(max_tram, running_sum)

        #* 3 
        #* 2-5 = -3 
        #* 4-2 = 2
        #* 4- 0 = 4

print(max_tram)

#* 4 

#* -0 + 3 = 3 

#* -2 + 5 = 6

#* - 4 + 2 = 4 

#* - 4 + 0 = 0

