'''
1. Fibonacci number
Problem Description

Write a program to read an integer (≥0) and output the corresponding Fibonacci number using recursion. An example is when the input integer is 5, the corresponding Fibonacci number, 5, will be shown as output.

Note: Fibonacci numbers are numbers in the Fibonacci sequence where the value of every number is the sum of the two preceding ones with the first two numbers as 0 and 1 respectively. For example, the first six Fibonacci numbers are 0,1,1,2,3,5. 

The Fibonacci number can be written as a formula: 

F(n) = F(n-1) + F(n-2) for n > 1

We can implement such function directly as a recursive function in Python:

def fib(n):
    return fib(n-1) + fib(n-2)
In order for a recursive function to work, we need to define a condition for it to terminate. For the case of Fibonacci number, we have two conditions, F(0)=0 and F(1)=1.

def fib(n):
    if n == 0 or n == 1:
        return n
        
    fn = fib(n-1) + fib(n-2)
    return fn
Complete the program by reading an integer from user and output the corresponding Fibonacci number.
'''
def fib(n):
    if n == 0 or n == 1:
        return n

    fn = fib(n-1) + fib(n-2)
    return fn

n = int(input())
print(fib(n))
