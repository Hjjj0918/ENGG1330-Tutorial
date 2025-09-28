# 1. Hailstone
# Problem Description :

# Douglas Hofstadter's Pulitzer-prize-winning book, Gödel, Escher, Bach, poses the following mathematical puzzle.

# Pick a positive integer n as the start.

# If n is even, divide it by 2.

# If n is odd, multiply it by 3 and add 1.

# Continue this process until n is 1.

# The number n will travel up and down but eventually, end at 1 (at least for all numbers that have ever been tried -- nobody has ever proved that the sequence will terminate). Analogously, a hailstone travels up and down in the atmosphere before eventually landing on earth.

# This sequence of values of n is often called a Hailstone sequence. Write a function that takes a single argument with formal parameter name n, prints out the hailstone sequence starting at n, and returns the number of steps in the sequence.

# Sample Input & Output

# Case 1

# input:

# 5
# output:

# 5
# 16
# 8
# 4
# 2
# 1
# 6

# Case 2

# input:

# 10
# output:

# 10
# 5
# 16
# 8
# 4
# 2
# 1
# 7
def hailstone(n):
    count = 0
    print(n)
    while (n != 1):
        if n % 2 == 1:
            n = n * 3 + 1
            print(int(n))
            count+=1
        else:
            n = n / 2
            print(int(n))
            count+=1
    return count+1
    
def main():
    n = int(input())
    a = hailstone(n)
    print(a)

main()