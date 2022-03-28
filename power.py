def calculate_power(x, y):
    # Complete this recursive function
    if(y==0):
        return 1 
    elif(y==1):
        return x 
    else:
        return (x*calculate_power(x,y-1))

a = int(input())
b = int(input())
# Call the calculate_power function
result = calculate_power(a,b)
print(result)