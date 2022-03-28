n=int(input())
row_output = "*" * (2*n)
print(row_output)

hallow_spaces_count =2

#for upper hallow diamond 

for row in range(1,n):
	asteriods_count = n - row
	asteriods = "*" * asteriods_count
	hallow_spaces= " " * hallow_spaces_count
	hallow_spaces_count += 2
	row_output = asteriods + hallow_spaces + asteriods
	print(row_output)  

for row_low in range(1,n):
	asteriods_count = row_low 
	asteriods = "*" * asteriods_count
	hallow_spaces_count -= 2
	hallow_spaces = " " * hallow_spaces_count
	row_output = asteriods + hallow_spaces + asteriods
	print(row_output)

row_output = "*" * (2*n)
print(row_output)