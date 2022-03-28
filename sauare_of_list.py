# square of given sequence and sort the result
# def sqr_of_list(list_a):
#     list_x = []
#     for i in list_a:
#         list_x += [i**2]
#     return list_x
# list_a = [2,4,1,3,5]
# result = sqr_of_list(list_a)
# print(sorted(result))
# print(sorted(result, reverse = True))

n = int(input())
list_a = []
for i in range(n):
    num = int(input())
    list_a.append(num)
print("input list is :{}".format(list_a))
list_b = []
for i in range(n):
    p = list_a[i]**2
    list_b.append(p)
print("output list is :{}".format(list_b))



