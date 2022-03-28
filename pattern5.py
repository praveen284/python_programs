n = int(input())
right_spaces_count = n-1
aster_count = 1
for i in range(n):
    right_spaces = right_spaces_count * " "
    aster = aster_count * "*"
    raw_output = aster + right_spaces
    print(raw_output)
    right_spaces_count -= 1 
    aster_count += 1
right_spaces_count = n-1
aster_count = 1 
for j in range(n):
    right_spaces = right_spaces_count * " "
    aster = aster_count * "*"
    raw_output = aster + right_spaces
    print(raw_output)
    aster_count += 1 
    right_spaces_count -= 1