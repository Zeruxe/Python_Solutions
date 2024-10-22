n = input()
n = int(n)

list = []

for i in range(n):
    word = input()
    if len(word) > 10:
        list.append(word[0] + str(len(word) - 2) + word[-1])
    else:
        list.append(word)

print("\n".join(list))