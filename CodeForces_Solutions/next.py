amount,pass_bar = input().split()
amount = int(amount)
pass_bar = int(pass_bar)
list = []
cnt = 0
                #- For some reason getting runtime error on test 4 which is not given
s = input().strip().split()
list.append(s)
#print(int(list[0][pass_bar]))
for i in range(amount):
    if int(list[0][i]) == 0:
        cnt == 0
    elif int(list[0][i]) >= int(list[0][pass_bar - 1]):
        cnt += 1


#sorted = s.sort()
print(cnt)