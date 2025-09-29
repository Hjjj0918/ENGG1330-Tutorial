# 2. Perfect Numbers
# Problem Description

# Write a Python program that reads two integers m and n where m < n and then outputs all the perfect numbers between m and n on the same line. If there's no perfect number, you may print out nothing.

# Perfect number: a perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself

# More about perfect number: perfect number - Wikipedia

# Sample Input&Output

# Note: the first number stands for m and the second one represents n .

# Case 1:

# Input

# 2 7
# Output

# 6
# Case 2:

# Input

# 1 28
# Output

# 6 28
def is_perfect(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num

def main():
    m, n = map(int, input().split())
    perfect_numbers = []
    for number in range(m, n + 1):
        if is_perfect(number):
            perfect_numbers.append(str(number))
    if perfect_numbers:
        print(" ".join(perfect_numbers))

main()