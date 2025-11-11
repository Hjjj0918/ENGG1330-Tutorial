inputa = []

inputa.append(input()) # find the number of rows by the length of the first input line
for i in range(len(inputa[0])-1): # minus 1 because the first line is already read
    inputa.append(input())


num_row = len(inputa)
num_col = len(inputa[0])
# initialize output array
output = [["0" for i in range(num_col)] for j in range(num_row)]

for i in range(num_row):
    for j in range(num_col):
        safe = 1
        supersafe = 1
        ii_range_safe = [-1,0,1]
        jj_range_safe = [-1,0,1]
        ii_range_supersafe = [-2,-1,0,1,2]
        jj_range_supersafe = [-2,-1,0,1,2]
        if i == 0: #uppermost line
            ii_range_safe = [0,1]
            ii_range_supersafe = [0,1,2]
        if i == num_row - 1: # lowermost line
            ii_range_safe = [-1,0]
            ii_range_supersafe = [-2,-1,0]
        if j == 0: # leftmost
            jj_range_safe = [0,1]
            jj_range_supersafe = [0,1,2]
        if j == num_col - 1:  # rightmost
            jj_range_safe = [-1,0]
            jj_range_supersafe = [-2,-1,0]
        if i == 1:
            ii_range_supersafe = [-1,0,1,2]
        if i == num_row - 2 :
            ii_range_supersafe = [-2,-1,0,1]
        if j == 1:
            jj_range_supersafe = [-1,0,1,2]
        if j == num_col - 2:
            jj_range_supersafe = [-2,-1,0,1]

        for ii in ii_range_safe:
            for jj in jj_range_safe:
                if inputa[i + ii][j+jj] == "1":
                    safe = 0
                    output[i + ii][j+jj] = "#"
        for ii in ii_range_supersafe:
            for jj in jj_range_supersafe:
                if inputa[i + ii][j + jj] == "1":
                    supersafe = 0

        if supersafe == 1:
            output[i][j] = "2"
        elif safe == 1:
            output[i][j] = "1"

for i in range(num_row):
    for j in range(num_col):
        if j < num_col - 1:
            print(output[i][j], end ="")
        else:
            print(output[i][j])
