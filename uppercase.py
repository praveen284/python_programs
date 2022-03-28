string = input().split(" ")
strin = ""
for i in string:
    if (string.index(i) == 0):
        strin += i.upper() +" "
    else:
        strin += i + " "
print(strin)