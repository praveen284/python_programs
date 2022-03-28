n=int(input("Enter the number :"))

#for left spacing
left_spaces = (n-1)
row_output= " " * left_spaces + "*"
print(row_output)

hallow_spaces_count = -1

# for upper triangle

for row in range(2,n+1):

	#for left spacing
	left_spaces_count = n - row
	left_spaces = " " * left_spaces_count
	
	#for spacing between *
	hallow_spaces_count = hallow_spaces_count + 2
	hallow_spaces = " " * hallow_spaces_count

	row_output = left_spaces + "*" + hallow_spaces + "*"
	print(row_output)

# for lower triangle

for row_low in range(1,n-1):

	#for left spacing
	left_spaces_count = row_low
	left_spaces = " " * left_spaces_count

	#for spacing between *
	hallow_spaces_count = hallow_spaces_count - 2
	hallow_spaces = " " * hallow_spaces_count
	row_output = left_spaces + "*" + hallow_spaces + "*"
	print(row_output)

#for left spacing
left_spaces = (n-1)
row_output= " "*left_spaces + "*"
print(row_output)


