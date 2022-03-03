n=int(input())
player=[int(x) for x in input().split()]
for x in player: 
    if x>2:
        player.remove(x)
    L=len(player)//3
print(L)