# half string lower

s = raw_input()
if(len(s)%2==0):
	n = len(s)//2
else:
	n = len(s)//2 + 1
p = s[:n]
for i in range(len(s)):
	if(i>=n):
		p += s[i].lower()
	else:
		continue
print(p)

print("\r")

# full string lower
u = ""
for i in range(len(s)):
		u += s[i].lower()
print(u)