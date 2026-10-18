## now we will study loops
i=1
while i<=5:
    print(i)
    i+=1
    pass
i=10
while i>=1:
    print(i)
    i-=1
pass
## now we will study break and continue
i=1
while i<=10: 
    if(i==5):
        i+=1
        break
    print(i)
    i+=1   
    pass
##nowe we use continue
i=1
while i<=10:
    if(i==5):
        i+=1
        continue
    print(i)
    i+=1