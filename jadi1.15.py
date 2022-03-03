for i in range(1,11):
    name=input()
    for j in range(0,len(name)):
        name=name.lower()
        name=name.replace(name[0],name[0].upper(),1)
    print(name)