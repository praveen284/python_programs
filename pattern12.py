n = int(input())
num = 0
for i in range(1,2*n):
        if(i<=n):
            num+=1
            print(num*"* ",end=" ")
           
        else:
            num-=1
            print(num*"* ",end=" ")
        print()