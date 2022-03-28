n = int(input())
num = n
total = 0
while(n!=0):
	temp = n%10
	total = (total*10) + temp
	n = n//10
if(total == num):
	print("Given number is palindrome")
else:
	print("given number is not palindrome")