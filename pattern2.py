n=int(input())

zeroes_count = -1

for row in range(1,n+1):
 	dots_count = n-row
 	dots = "." * dots_count
 	zeroes_count += 2
 	zeroes = "0" * zeroes_count
 	row_output = dots + zeroes + dots
 	print(row_output)

for row_low in range(1,n):
 	dots_count = row_low
 	dots = "." * dots_count
 	zeroes_count -= 2
 	zeroes = "0" * zeroes_count
 	row_output = dots + zeroes + dots
 	print(row_output)



