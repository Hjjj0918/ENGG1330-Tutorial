# 2. Largest Factor
# Problem Description :

# Write a function that takes an integer n that is greater than 1 and returns the largest integer that is smaller than n and evenly divides n.

# Sample Input & Output

# Case 1

# input:

# 15
# output:

# 5
# Note: factors for 15 are 1, 3, 5. 

# Case 2

# input:

# 13
# output:

# 1
def largest_factor(n):
    for i in range(n-1, 0, -1):  
        if n % i == 0:
            return i

def main():
    n = int(input())
    print(largest_factor(n))

main()