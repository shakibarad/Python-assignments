name=input()
vovels="eiouAEIOUa"
name=name.lower()
new_name=""
print(new_name)
for letter in name:
    if letter in vovels:
        new_name+=""
    else:
        new_name+="."+letter
print(new_name)
