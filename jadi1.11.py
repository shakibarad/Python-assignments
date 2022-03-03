max1=11
max2=10
number= 2
while number!=-1:
    number= int(input())
    if number>max1:
        max2=max1
        max1=number
    elif number>max2:
        max2=number
        
            
print(max1,"",max2)