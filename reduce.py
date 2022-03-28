from functools import reduce
def sum_of_items(a,b):
    return a+b 
    
list_a = [1,2,3,4,5]
sum_of_list = reduce(sum_of_items,list_a)
print(sum_of_list)