n = int(input())
spaces_count = n - 2
print("* "*n)
for i in range(n-2):
    spaces = spaces_count * "  "
    output = "* " + spaces + "* "
    print(output)
print("* "*n)
spaces_count = n*2 - 2
for i in range(n-2):
    spaces = spaces_count * " "
    output = spaces + "* "
    print(output)
print("* "*n)