def fib(n):
    if n == 0 or n == 1:
        return n

    fn = fib(n-1) + fib(n-2)
    return fn

n = int(input())
print(fib(n))
