# n = int(input("Enter an positive integer value for n:"))
# total = 0
# temp = n
# while(temp>0):
# 	digit = temp %10
# 	total += digit**3
# 	temp //= 10
# if(total == n):
# 	print("Given number {} is armstrong number".format(n))
# else:
# 	print("Given number {} is not armstrong number".format(n))


def armstrong(n):
	total = 0
	temp = n
	while(temp>0):
		digit = temp %10
		total += digit**3
		temp //= 10
	if(total == n):
		return ("Given number {} is armstrong number".format(n))
	else:
		return ("Given number {} is not armstrong number".format(n))
n = int(input("Enter an positive integer value for n:"))
result = armstrong(n)
print(result)


