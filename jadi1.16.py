name=input()
kod="hello"
T=-1
a=0
for i in kod:
    if i not in name[T+1:]: 
        a=1
        break
    else:
        T=T+1+name[T+1:].find(i)
if a==1:
    print("NO")
else:
    print("YES")