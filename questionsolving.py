num=[1,2,3,4,5]
rev=[]
for i in range(len(num)-1,-1,-1):
    rev.append(num[i])
print(rev)
num=[1,2,3,4,5]
even=[]
odd=[]
for i in num:
    if(i%2==0):
        i=even.append(i)
     
    elif(i%2!=0):
        i=odd.append(i)    
print("even",even)
print("odd",odd)