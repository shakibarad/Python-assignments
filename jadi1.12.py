def maghsoom(x,k):
    for j in range(1,x+1):
        if x%j==0:
            k+=1
    return(k)



max=1
number_max=2
for i in range(20):
    number=int(input())
    k=0
    k= maghsoom(number,k)
    if k>max:
        number_max=number
        max=k
    elif k==max:
        if number_max<number:
            number_max=number
            
print(number_max,"",max)