name=input()
name1=name.find("AB")
name2=name[name1 + 2:].find("BA")
if name1>=0 and name2>=0 :
     print("YES")
else:
    name1=name.find("BA")
    name2=name[name1 + 2:].find("AB")
    if name1>=0 and name2>=0:
        print("YES")
    else:
        print("NO")
