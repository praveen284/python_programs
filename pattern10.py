n = int(input())
spaces_count = 2*(n-1)
asters_count = 1 
for i in range(n):
    spaces = spaces_count * " "
    asters = asters_count * "* "
    out = asters + spaces + spaces + asters
    print(out)
    spaces_count -= 2
    asters_count +=1
for i in range(n):
    spaces_count += 2
    asters_count -=1
    spaces = spaces_count * " "
    asters = asters_count * "* "
    out = asters + spaces + spaces + asters
    print(out)