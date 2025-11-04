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
