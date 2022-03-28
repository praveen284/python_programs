n=int(input())

hollow_space_count = 0
for row in range(1,n+1):
	space_count = n-row
	space = " " * space_count
	hollow_space = " " * hollow_space_count
	row_output = space + "/" + hollow_space + "\\"
	hollow_space_count += 2
	print(row_output)

for row_low in range(0,n):
	space_count = row_low
	space = " " * space_count
	hollow_space_count -= 2
	hollow_space = " " * hollow_space_count
	row_output = space + "\\" + hollow_space + "/"
	print(row_output)

