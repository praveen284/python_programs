# sum of natural numbers using recursion

def sum_n(n):
	if(n==0):
		return 0
	return n + sum_n(n-1)
n = int(input("Enter value for n:"))
result = sum_n(n)
print("sum of natural numbers upto {} is {}".format(n,result))

# using loop

# n = int(input("Enter value for n:"))
# sum = 0
# for i in range(n+1):
# 	sum += i 
# print("sum of natural numbers upto {} is {}".format(n,sum))
