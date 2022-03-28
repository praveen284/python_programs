#Hollow right triangle

n = int(input())
print(n*"* ")
left_spaces = 1
middle_spaces = n-3  
for i in range(n-2):
    spaces = left_spaces * "  "
    middle_space = middle_spaces*"  "
    out = spaces + "* " +  middle_space + "* "
    print(out)
    left_spaces+=1 
    middle_spaces-=1 
spaces = left_spaces *"  "
out = spaces + "* "
print(out)


