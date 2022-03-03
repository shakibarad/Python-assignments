A=[]
import math
n=int(input())
for i in range(0,n):
    for x in input().split():
        x=float(x)
        A.append(x)

for j in A:  
    Laptop=math.sqrt(j)
    print('{:.5f}'.format(Laptop)[:-1])