n = list(map(str, input().replace(" ", "").lower()))


for i in range(len(n)):
    if n[-2] == 'a' or n[-2] == 'e' or n[-2] == 'i' or n[-2] == 'o' or n[-2] == 'u' or n[-2] == 'y':
        print("YES")
        break
    else:
        print("NO")
        break

#- This below also works in the first if statement  
#* if n[-2] in {'a', 'e', 'i', 'o', 'u', 'y'}:
