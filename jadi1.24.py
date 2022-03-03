counter=dict()
A=[]
n=int(input())
for i in range(0,n):
    country=[x   for x in input().split()]
    A.append(country)
sentence=input()
B=sentence.split()
for x in A:
    counter[x[0]]=x[1]
for t in range(0,len(B)):
    kl=B[t]
    if kl in counter.keys():
        B[t]=counter[kl]
          
print(" ".join(B))