N, M = input().split()
N = int(N)
M = int(M)
queen = []
for i in range(M):
    x, y = input().split()
    queen.append([int(x)-1,int(y)-1])

chess = [[1 for j in range(N)] for i in range(N)]
for i in range(M):
    x,y = queen[i][0], queen[i][1]
    for j in range(N):
        chess[x][j] = 0
        chess[j][y] = 0
    for m in range(1,min(x+1,y+1)):
        chess[x-m][y-m] = 0
    for m in range(1,min(N-x,N-y)):
        chess[x+m][y+m] = 0
    for m in range(1,min(N-x,y+1)):
        chess[x+m][y-m] = 0
    for m in range(1,min(x+1,N-y)):
        chess[x-m][y+m] = 0

count = 0
for i in range(N):
    for j in range(N):
        count += chess[i][j]
print(count)