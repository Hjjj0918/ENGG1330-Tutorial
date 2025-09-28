# 1. Remove Duplicates
# Problem Description

# You will be given a sorted list of numbers in non-decreasing order. Try to remove duplicates and the order of the numbers should be maintained.

# set() is not allowed to use for this question

# Sample Input/Output

# Case 1

# Input

# 1 2 2 3 3 3 4 4 4 4
# Output

# [1, 2, 3, 4]
# Case 2

# Input

# 6 6 7 8 8
# Output

# [6, 7, 8]
def remove_duplicates(numList):

    i = 0
    while(i < len(numList) - 1):
        if(numList[i] != numList[i + 1]):
            i += 1
        else:
            numList.pop(i)

    return numList    


def main():

    numList = input().split()
    numList = list(map(int, numList))
    print(remove_duplicates(numList))

main()