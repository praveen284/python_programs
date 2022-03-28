
def isPalindrome(s):
	s = s.lower()
	l = len(s)
	if(l<2):
		return True
	elif(s[0]==s[l - 1]):
		return isPalindrome(s[1:l-1])
	else:
		return False

s = input()
a = isPalindrome(s)
if(a):
	print("Yes")

else:
	print("No")
