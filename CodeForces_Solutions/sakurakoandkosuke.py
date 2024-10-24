n = int(input())
#* + = Kosutke, - = Sakurako 

list = []

for i in range(n):
    x = int(input())
    if x % 2 == 0:
        list.append("Sakurako")
    else:
        list.append("Kosuke")

print("\n".join(list)) #print in normal format to the standard output