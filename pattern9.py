n = int(input())
print((2*n-1)*"* ")
spaces_count = 0
spaces_middle_count = 0
asters_count = n-1
for i in range(n-1):
    spaces = spaces_count * " "
    asters  = asters_count * " *"
    spaces_middle = spaces_middle_count * " "
    out = spaces + asters + spaces_middle + asters +spaces
    print(out)
    spaces_count += 1 
    spaces_middle_count += 2
    asters_count -= 1