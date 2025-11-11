n = int(input())
tank = list(map(int, input().split()))
current = int(input())


final = [0] * n # 0 - empty, 1 - filled

while final[current] < 1: # while the tank is not yet filled
    final[current] += 1 # fill the tank
    current = tank[current] # move to the next tank
     
    if current == -1:
        break
  
print(sum(final))