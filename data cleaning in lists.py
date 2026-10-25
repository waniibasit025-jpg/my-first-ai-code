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
