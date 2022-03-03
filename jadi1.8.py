number= int(input())

for i in range (2,number):
    B= number%i
    if B==0:
        print("not prime")
        break
if B!=0:
    print("prime")