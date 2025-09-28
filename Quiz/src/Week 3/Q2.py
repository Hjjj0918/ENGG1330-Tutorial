# 2. Sum Digits
# Problem Description

# Write a function that takes in a non-negative integer and sums its digits.

# Sample Input&Output

# Case 1

# input:

# 10
# output:

# 1
# Case 2

# input:

# 4224
# output:

# 12
# Case 3

# input:

# 1234567890
# output:

# 45
# Case 4

# input:

# 123
# output:

# 6
def sum_digits(y):
    total = 0
    while y > 0:
        total, y = total + y % 10, y // 10
    return total
    
def main():
    y = int(input())
    print(sum_digits(y))

main()