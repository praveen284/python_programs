# Greatest Palindrome in a String


n=input()
l=[]
for i in range(len(n)):
	for j in range(i,len(n)):
		if(n[i:j]!=" " and n[i:j] not in l):
			l.append(n[i:j])
gst=""
j=0
for i in l:
	p=i 
	if(i[::-1]==p):
		if(len(i)>=j):
			j=len(i)
			gst=i
print(gst)