name=input()
K=0
B=0
for i in name:
    if i.upper()<i:
        K+=1
    elif i.upper()==i:
        B+=1
    else:
         B+=1
    if B>K:
        name=name.upper()
    else:
        name=name.lower()
print(name)