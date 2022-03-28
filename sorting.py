n=int(input())
k=[]
for i in range(n):
    j=int(input())
    k.append(j)
for i in range(len(k)):
    for j in range(i,len(k)):
        if(k[i]<k[j]):
            temp = k[i]
            k[i]=k[j]
            k[j]=temp
for i in k:
    print(i)