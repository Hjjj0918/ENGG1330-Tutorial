# 2. Find The Number
# Problem Description

# You will be given a list of n numbers ranging from 0 to n. Find the only number that is not inside the list.

# Sample Input/Output

# Case 1

# Input

# 1 2 3
# Output

# 0
# Case 2

# Input

# 4 0 1 3
# Output

# 2
def find_number(numList):

    """
    *This method is not recommended*
    """
    n = len(numList)
    return ((n * (n+1)) // 2) - sum(numList)


def main():

    numList = input().split()
    numList = list(map(int, numList))
    print(find_number(numList))

main()