#missing letter
def find_num(n):
    l=len(n)+1
    p=l*(l+1)/2 - sum(n)
    return p
n=[ 1,2,3,4,5,6,7,8,10]
p=find_num(n)
print (p)

#last digit of given number
def find_num(n):
    p=n%10
    return int(p)
   
n=int(input("Enter the number:"))
p=find_num(n)
print (p)


#check 5 is present or not
def check_num(n):
    for i in range(len(n)):
        if(n[i]==5):
            p="found"
            return p
        else:
            continue
n=[ 1,2,3,45,5,6,7,8,10]    
p=check_num(n)
print (p)
