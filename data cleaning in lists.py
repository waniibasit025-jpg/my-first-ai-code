###we have to remove all this "" and print pure data.//
data=["apple","","banana",""]
while "" in data:
    data.remove("")
print(data)    
pass
##replace junk with unknown
data=["ali","",None,"sara",""]
new_data=[]
for i in data:
    if i=="" or  i==None:
        new_data.append("Unknown")
    else:
        new_data.append(i)
print(new_data) 
pass
## now we will find the maximum and minumum with out min and max function..//
a=[1,2,3,44,55,66,44] 
max_val=a[0]
min_val=a[0]
for i in a:
    if i>max_val:
        max_val=i

    elif i<min_val:
        min_val=i
print("maximum:",max_val)
print("minimum:",min_val)                 
