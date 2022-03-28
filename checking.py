# program to check if a string has at least one letter and one number and space 

def checkString(str):
	
	flag_a = False
	flag_n = False
	flag_s = False
	
	for i in str:
		# if string has letter
		if i.isalpha():
			flag_a = True

		# if string has number
		if i.isdigit():
			flag_n = True

		if i == " ":
			flag_s = True

	return flag_a and flag_n and flag_s


# driver code
s = raw_input()
print(checkString(s))
print(checkString('geeksforgeeks'))
