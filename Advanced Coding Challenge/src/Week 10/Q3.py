'''
Compute the factorial of an input number (≥0, <10) using recursion. 
'''
def fact(n):
    if n <= 1:
        return 1

    return n * fact(n-1)

print(fact(int(input())))