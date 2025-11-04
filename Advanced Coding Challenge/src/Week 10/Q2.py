'''
2. Fibonacci number illustration
Problem Description

Modify the program in the Fibonacci number exercise to also show the process of finding Fibonacci number using recursion. For example if the input number is 2, the code should output:

calculate f 2
f 2 = f 1 + f 0
calculate f 1
return 1
calculate f 0
return 0
f 2 = 1
return 1
1

The last line of output is the result of printing the output of fib(), which is the original output in the last exercise.

If the input number is 3, the code should output:

calculate f 3
f 3 = f 2 + f 1
calculate f 2
f 2 = f 1 + f 0
calculate f 1
return 1
calculate f 0
return 0
f 2 = 1
return 1
calculate f 1
return 1
f 3 = 2
return 2
2

To start with, we can print the statement “calculate f n” whenever the function is called to see how many times the function is called.

def fib(n):
    print('calculate f', n)
    ...
If you run the code and input 2, you will see the following output:

calculate f 2
calculate f 1
calculate f 0
We get this result because when we calculate fib(2), it will execute fib(1) and fib(0). Since both fib(1) and fib(0) are terminal cases, no further fib() is called.

Can you predict the result of calling fib(3) ?

If you run the code and input 3, you will see the following output:

calculate f 3
calculate f 2
calculate f 1
calculate f 0
Calculate f 1
fib(3) will call fib(2) and fib(1), fib(2) gives line 2 to 4 of the output, and fib(1) gives the last line in the output.

To complete this task, try to add the following print-out in the function. After adding each of the print-out, predict the result and validate your answer by running the code.

Add a “return x” before returning a value in fib(), where x is the return value. 

Add “f n = f n-1 + f n-2” if fib() is called in the case of n > 1. Print this message after the message “calculate f n”.

Add “f n = x” when the result of fib(n) is calculated in the case of n > 1.
'''
def fib(n):
    print('calculate f', n)
    if n == 0 or n == 1:
        print('return', n)
        return n

    print(f'f {n} = f {n-1} + f {n-2}')
    x = fib(n-1) + fib(n-2)
    print(f'f {n} = {x}')
    print('return', x)
    return x

n = int(input())
print(fib(n))
