n=int(input())
l=[]
for i in range(n):
	p=int(input())
	l.append(p)
for i in range(n):
   m= i
   for j in range(i+1,n):
      if(l[m]>l[j]):
         m=j
   temp=l[i]
   l[i]=l[m]
   l[m]=temp
print(l)