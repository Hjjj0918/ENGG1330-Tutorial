def nCk(n, k):
    if n < k:
        return 0

    if k == 0 or k == n:
        print(f'{n}C{k} = 1')
        return 1

    print(f'{n}C{k} = {n-1}C{k-1} + {n-1}C{k}')
    x = nCk(n-1, k-1) + nCk(n-1, k)
    print(f'{n}C{k} = {x}')
    return x

nCk(int(input()), int(input()))
