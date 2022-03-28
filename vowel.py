s="PraveenJayamma"
l=["a","e","i","o","u","A","E","I","O","U"]
c=0
p=0
for i in s:
	if(i in l):
		c+=1
	else:
		p+=1
print(c)
print(p)