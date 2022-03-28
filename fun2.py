#extracting digits of given sequence and finding the sum,min,max values
def get_digits(list_a):
    list_b = []
    for i in list_a:
        if(i.isdigit()==True):
            list_b += [int(i)] 
        else:
            continue
    return list_b
        
str_a = input("Enter a string:")
list_a = list(str_a)
print(list_a)
result = get_digits(list_a)
print(result)
sum_of_digits = sum(result)
max_of_digits = max(result)
min_of_digits = min(result)
len_of_digits = len(result)
sort_of_digits = sorted(result)
rev_sort_of_digits = sorted(result, reverse = True)

print("sum of sequence is : ",sum_of_digits)
print("max value of sequence is : ",max_of_digits)
print("min value of sequence is : ",min_of_digits)
print("length  of sequence is : ",len_of_digits)
print("sorting of sequence is : ",sort_of_digits)
print("reverse sorting of sequence is : ",rev_sort_of_digits)

