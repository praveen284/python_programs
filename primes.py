# prime numbers between n and m

n = int(input("Enter an positive integer value for n:"))
m = int(input("Enter an positive integer value for m :"))
if(n<=m):
    for num in range(n,m+1):
        if(num>1):
            for i in range(2,num):
                if(num%i==0):
                    break
            else:
                print("{} is a Prime Number".format(num))
else:
    print("Enter valid inputs for m & n (n<m)")



# def primes(n,m):
#     if(n<=m):
#         for num in range(n,m+1):
#             count = 0
#             if(num>1):
#                 for i in range(1,num+1):
#                     if(num%i==0):
#                         count += 1
#                 if(count==2):
#                     print("{} is a Prime Number".format(num))
#     else:
#         print("Enter valid inputs for m & n (n<m)")


# n = int(input("Enter an positive integer value for n:"))
# m = int(input("Enter an positive integer value for m :"))
# primes(n,m)


# sum of primes between n and m

# def primes(n,m):
#     sum = 0
#     if(n<=m):
#         for num in range(n,m+1):
#             count = 0
#             if(num>1):
#                 for i in range(1,num+1):
#                     if(num%i==0):
#                         count += 1
#                 if(count==2):
#                     sum += num
#         return sum
#     else:
#         return ("Enter valid inputs for m & n (n<m)")


# n = int(input("Enter an positive integer value for n:"))
# m = int(input("Enter an positive integer value for m :"))
# result = primes(n,m)
# print("sum of prime numbers m to n is {}".format(result))