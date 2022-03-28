# counting the number of words ending with alphabet a in given string

string = input()
string_a = string.split()
count = 0
for i in range(len(string_a)):
    if(string_a[i][len(string_a[i])-1] =="a"):
        count +=1 
print(count)


# replace of with ok in given string

string = input()
string_a = string.split()
new_string = ""
for i in string_a:
    if(i == "of"):
        new_string += "ok "
    else:
        new_string += i+" "
print(new_string)

    
