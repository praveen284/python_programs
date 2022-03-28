#finding the largest number  of given input string

def max_of_list(list_a):
    list_x = []
    for i in list_a:
        if(i.isdigit()):
            list_x += [i]
        else:
            continue
    return list_x
str_a = input()
list_a = list(str_a.split(","))
result = max_of_list(list_a)
print(max(result))
print(sorted(result))
print(sorted(result, reverse = True))


# def max_of_list(list_a):
#     list_x = []
#     for i in list_a:
#         if(i.isdigit()):
#             list_x += [i]
#         else:
#             continue
#     return sorted(list_x)
# str_a = input()
# list_a = list(str_a.split(","))
# result = max_of_list(list_a)
# print(result[-1])