#Consecutive vowels in a string

n=input()
l=['a','e','i','o','u']
v=[]
for i in range(len(n)):
	if(n[i] in l):
		v.append(n[i])
print(v)
count=0
for i in range(len(n)-1):
	if(n[i] in l):
		if(n[i+1] in l):
			count+=1
print(count)