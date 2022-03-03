A=[]
n=int(input())
for i in range(0,n):
    Laptop=[int(x) for x in input().split()]
    A.append(Laptop)
#print(A)
a=0
for j in range(0,len(A)):
    for t in range(0,len(A)-1):
        if (A[j][0]<A[t+1][0] and A[j][1]>A[t+1][1]) or (A[j][0]>A[t+1][0] and A[j][1]<A[t+1][1]):
            a+=1
if a>=1:
    print("happy irsa")
else:
    print("poor irsa")