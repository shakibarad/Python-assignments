name=input()
min=100
j=""
for jj in range(0,len(name)):
    for i in name:
        if i!="+":
            if int(i)<=min:
                min=int(i)           
    C = name.count(str(min))
    j+= C*(str(min))
    name=name.replace(str(min),"+")
    min=100
M = ""
for i in range(len(j)):
    if i==len(j)-1:
        M+=j[i]
    else:
        M+=j[i]+"+"    
print(M)