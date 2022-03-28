# nth term of fibonacci series

# def fibonacci(n):
#     if(n==0):
#         return 0
#     if(n==1):
#         return 1 
#     return fibonacci(n-1) + fibonacci(n-2)

# n=int(input("Enter a positive integer value for n :"))
# result = fibonacci(n)
# print(result)

def fibonacci(n):
    list_a =[]
    if(n==0):
        list_a.append(0)
    if(n==1):
        list_a.append(1)
    else:
        n1 = 0
        n2 = 1
        for i in range(n):
            nth = n1 + n2
            list_a.append(nth)
            n1 = n2
            n2 = nth
    return list_a
n=int(input("Enter a positive integer value for n :"))
result = fibonacci(n)
print("fibonacci sequence is : {}".format(result))
print("nth term of fibonacci sequence is:{}".format(result[n-1]))

