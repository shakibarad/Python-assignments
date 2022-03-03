data_list = [ int(x) for x in input().split() ]
data_list.sort()
c=max(data_list)
v=min(data_list)
n=c-v
 
print(n)
    