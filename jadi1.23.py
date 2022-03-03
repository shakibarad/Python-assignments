counter=dict()
A=[]
n=int(input())
for i in range(0,n):
    country= input()
    A.append(country)
for x in A:
    counter[x]=counter.get(x,0)+1
keyss = list(counter.keys())
keyss.sort()
for j in keyss:
    print(" ".join((j,str(counter[j]))))