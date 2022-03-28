# filter(function,sequence)
def is_positive_number(n):
    return n>0
        
list_a = [-2,1,2,3,4,-9,-3]
positive_number = filter(is_positive_number,list_a)
print(list(positive_number))
        