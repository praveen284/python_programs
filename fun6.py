# kth largest number of given list_a
def kth_letter_of_list(list_a):
    list_x = []
    for i in list_a:
        if(i.isdigit()):
            list_x += [i]
        else:
            continue
    k = int(input())
    if(k<=len(list_x)):
        return (sorted(list_x)[-k+1])
str_a = input()
list_a = list(str_a.split(","))
result = kth_letter_of_list(list_a)
print(result)


# kth largest number of given list_a
def kth_letter_of_list(list_a):
    list_x = []
    for i in list_a:
        if(i.isdigit()):
            list_x += [i]
        else:
            continue
    k = int(input())
    if(k<=len(list_x)):
        return (sorted(list_x, reverse = True)[k-1])
str_a = input()
list_a = list(str_a.split(","))
result = kth_letter_of_list(list_a)
print(result)

