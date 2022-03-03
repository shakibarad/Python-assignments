import random
l=1
u=99
hads= random.randint(l,u)
print(hads)
javab=input()
while javab!="d":
    if javab=="b":
        u=hads-1
        hads=random.randint(l,u)
        print(hads)
    elif javab=="k":
        l=hads+1
        hads=random.randint(l,u)
        print(hads)
    javab=input()
