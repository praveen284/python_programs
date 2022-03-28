# factorial of given num

# def compute_factorial(n):
#     # Complete this recursive function
#     if(n==0):
#         return 1 
#     fact = n * compute_factorial(n-1)
#     return fact

# n = int(input())
# # Call the compute_factorial function
# result = compute_factorial(n)
# print(result)

n = int(input("Enter a positive integer value for n:"))
if(n==0):
    print("factorial of {} is 1".format(n))
fact = 1
for i in range(1,n+1):
    fact *= i 
print("factorial of {} is {}".format(n,fact))

