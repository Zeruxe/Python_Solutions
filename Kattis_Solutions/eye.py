n = input()

before = n.split("(")[0]
after = n.split(")")[1]

if len(before) == len(after):
    print("correct")
else:
    print("fix")
