n=int(input())
l=[]
for i in range(n):
	p=int(input())
	l.append(p)
for i in range(n-1): #for number of iterations  
        for j in range(n-1):  
            if(l[j]>l[j+1]):  
                temp = l[j]  
                l[j] = l[j+1]  
                l[j+1] = temp  
print(l) 