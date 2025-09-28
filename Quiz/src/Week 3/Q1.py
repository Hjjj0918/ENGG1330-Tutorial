# 1. Falling Factorial
# Problem Description

# Let's write a function falling, which is a "falling" factorial that takes two arguments, n and k, and returns the product of k consecutive numbers, starting from n and working downwards. When k is 0, the function should return 1.

# Sample Input&Output

# Case 1

# input:

# 6 3
# output:

# 120
# Case 2

# input:

# 4 3
# output:

# 24
# Case 3

# input:

# 4 1
# output:

# 4
def falling(n, k):
    sum = 1
    while k > 0:
        sum *= n
        k = k - 1
        n = n - 1
    return sum

def main():
    n, k = input().split()
    n = int(n)
    k = int(k)
    print(falling(n,k))

main()