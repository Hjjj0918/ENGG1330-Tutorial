def rot_clockwise(x, n):
    row,col = len(x),len(x[0])
    y = [['0' for j in range(col)] for i in range(row)]
    if n==90:
        for i in range(row):
            for j in range(col):
                y[i][j] = x[row-1-j][i]
    return y

def find_treas(treas, mymap):
    flag = 0
    for i in range(len(mymap)-len(treas)+1):
        for j in range(len(mymap[0])-len(treas[0])+1):
            flag = 1
            for m in range(len(treas)):
                for n in range(len(treas[0])):
                    if treas[m][n]!=mymap[m+i][n+j]:
                        flag = 0
            if flag==1:
                print(j,i)
                return flag
    return flag

def search(x, y):
    rot0 = x
    rot90 = rot_clockwise(rot0,90)
    rot180 = rot_clockwise(rot90,90)
    rot270 = rot_clockwise(rot180,90)
    if find_treas(rot0, y)==1:
        return
    elif find_treas(rot90, y)==1:
        return
    elif find_treas(rot180, y)==1:
        return
    elif find_treas(rot270, y)==1:
        return
    else:
        return

treas = []
treas.append(input())
for i in range(len(treas[0])-1):
    treas.append(input())


mymap = []
mymap.append(input())
for i in range(len(mymap[0])-1):
    mymap.append(input())
    
#print(mymap)

#rot0 = np.array(rot_clockwise(treas,0))
#rot90 = np.array(rot_clockwise(treas,90))
#rot180 = np.array(rot_clockwise(treas,180))
#rot270 = np.array(rot_clockwise(rot180,90))

search(treas, mymap)