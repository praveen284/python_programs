# n = int(input("Enter an integer number :"))
# count = 0
# for i in range(2,n):
# 	if(n%i == 0):
# 		count += 1
# if(count == 0):
# 	print("Given number {} is a prime number".format(n))
# else:
# 	print("Given number {} is not a prime number".format(n))

def prime(n):
	count = 0
	for i in range(2,n):
		if(n%i == 0):
			count += 1
	if(count == 0):
		return ("Given number {} is a prime number".format(n))
	else:
		return ("Given number {} is not a prime number".format(n))

n = int(input("Enter an positive integer value for n:"))
m = int(input("Enter an positive integer value for m :"))
result = prime(n)
sol = prime(m)
print(result)
print(sol)