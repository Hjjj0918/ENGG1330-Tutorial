# 1. Intersection
# Problem Description

# You will be given a list of lists and you are expected to find a list of distinct elements that appear in all lists. If there's no such element, return an empty list.

# Sample Input&Output

# The input part is all set for you. The following input is what it looks like in the function itself.

# Case 1:

# Input

# [['1', '2', '3'], ['1', '3', '5']]
# Output

# ['1', '3']
# Case 2:

# Input

# [['1', '2', '3'], ['4', '5'], ['7', '8', '9', '10']]
# Output

# []
def intersection(lsts):

    elements = []
    for elem in lsts[0]:
        condition = elem not in elements
        for lst in lsts[1:]:
            if elem not in lst:
                condition = False
        if condition:
            elements = elements + [elem]
    return elements

def main():

    lsts = []
    num = int(input())
    for _ in range(num):
        tempList = input().split()
        lsts.append(tempList)
    print(intersection(lsts))

main()