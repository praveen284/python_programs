#exampke for recursion function

def multiply(n):
    if(n==1):
        return 1
    return n * multiply(n-1)
num = int(input())
result = multiply(num)
print(result)



#exampke for recursion function
def sum_of_numbers(n):
    if(n==0):
        return 0
    else:
        return n + sum_of_numbers(n-1)
num = int(input())
result = sum_of_numbers(num)
print(result)