a=0
name=input()
name=name.upper()
for i in range(0,len(name)):
    if name[i]!=name[len(name)-i-1]:
        a=1
        break   
if a==0:
    print("palindrome")
else:
    print("not palindrome")