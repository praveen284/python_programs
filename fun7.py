#call stack functions 
def nums_sqr(x):
    return (x**2)
def sum_of_squares(list_a):
    sqr_sum = 0
    for i in list_a:
        sqr_sum = nums_sqr(i)
    return sqr_sum
list_a = [1,2,4,-5]
sum_of_sqares = sum_of_squares(list_a)
print(sum_of_sqares)