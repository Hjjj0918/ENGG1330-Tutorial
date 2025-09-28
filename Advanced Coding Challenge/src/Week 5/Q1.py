# 1. Permutation
# Problem Description

# You will be given a sorted list of numbers (numbers are unique), and you need to print out all permutations in increasing lexicographical order.

# Sample Input & Output

# Case 1

# Input

# 1 2 3
# Output

# ['1', '2', '3']
# ['1', '3', '2']
# ['2', '1', '3']
# ['2', '3', '1']
# ['3', '1', '2']
# ['3', '2', '1']
# Case 2

# Input

# 1 2 3 4
# Output

# ['1', '2', '3', '4']
# ['1', '2', '4', '3']
# ['1', '3', '2', '4']
# ['1', '3', '4', '2']
# ['1', '4', '2', '3']
# ['1', '4', '3', '2']
# ['2', '1', '3', '4']
# ['2', '1', '4', '3']
# ['2', '3', '1', '4']
# ['2', '3', '4', '1']
# ['2', '4', '1', '3']
# ['2', '4', '3', '1']
# ['3', '1', '2', '4']
# ['3', '1', '4', '2']
# ['3', '2', '1', '4']
# ['3', '2', '4', '1']
# ['3', '4', '1', '2']
# ['3', '4', '2', '1']
# ['4', '1', '2', '3']
# ['4', '1', '3', '2']
# ['4', '2', '1', '3']
# ['4', '2', '3', '1']
# ['4', '3', '1', '2']
# ['4', '3', '2', '1']
from itertools import permutations
def print_permutations(numList):
    perm = permutations(numList)
    for p in perm:
        print(list(p))

def main():
    numList = input().split(" ")
    print_permutations(numList)
main()