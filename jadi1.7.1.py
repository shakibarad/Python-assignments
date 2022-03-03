import random
l=1
u=99
javab= int(input())
hads= random.randint(l,u)
while hads!=javab:
    if hads>javab:
        u=hads-1
    else:
        l=hads+1
    hads=random.randint(l,u)
    print(hads)
print("done!")