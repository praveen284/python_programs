#finding the largest number  of given input string

def min_of_list(list_a):
    list_x = []
    for i in list_a:
        if(i.isdigit()):
            list_x += [i]
        else:
            continue
    return list_x
str_a = input()
list_a = list(str_a.split(","))
result = min_of_list(list_a)
print(min(result))
print(sorted(result))
print(sorted(result, reverse = True))


# def min_of_list(list_a):
#     list_x = []
#     for i in list_a:
#         if(i.isdigit()):
#             list_x += [i]
#         else:
#             continue
#     return sorted(list_x)
# str_a = input()
# list_a = list(str_a.split(","))
# result = min_of_list(list_a)
# print(result[0])

# num=input()
# num_list=num.split(",")
# len_list=len(num_list)
# for i in range(len_list):
#     num_list[i] = int(num_list[i])
# num_list=sorted(num_list)
# print(min(num_list))