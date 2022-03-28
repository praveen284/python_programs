n=int(input())
l=[]
for i in range(n):
	p=int(input())
	l.append(p)
print(l)
m=l[0]
for i in range(1,n-1):
	if(l[i]>m):
		m=l[i]
h=0
for i in range(n):
	if(l[i]!=m and l[i]>h):
		h=l[i]
print(h)
