'''
1. Binary Strings
Problem Description

Given an integer n, print out all possible cases of n-bit binary strings in increasing order.

Hint: use recursion

Sample Input & Output

Case 1

Input:

2
Output:

[0, 0]
[0, 1]
[1, 0]
[1, 1]
Input:

3
Output:

[0, 0, 0]
[0, 0, 1]
[0, 1, 0]
[0, 1, 1]
[1, 0, 0]
[1, 0, 1]
[1, 1, 0]
[1, 1, 1]
'''
def binStr(n:int, prev:list):
    if len(prev) == n:
        print(prev)    

    else:
        binStr(n, prev + [0])
        binStr(n, prev + [1])


def main():
    n = int(input())
    binStr(n, [])

main()