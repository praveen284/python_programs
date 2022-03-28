# swapping of two numbers without third variable

n = int(input("Enter an  integer value for n:"))
m = int(input("Enter an  integer value for m :"))

# using arthematic
# m = m+n 
# n = m - n 
# m = m - n 
# print("({},{}) after swapping ({},{})".format(m,n,n,m))


# using divison and multiplicaton
m = m*n 
n = m // n 
m = m // n 
print("({},{}) after swapping ({},{})".format(m,n,n,m))