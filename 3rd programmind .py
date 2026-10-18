### in this we will  make some small project on if else elif conditions,.///
age=int(input("age:"))
if(age==18):
    print("can vote")
if(age<18):
    print("minor can not vote")    
elif(age<=45):
    print("can also vote ")    
else:
    print("can not vote old")    
 ##### mini question on even odd number
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