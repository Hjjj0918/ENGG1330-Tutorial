'''
Implement the Combinations by the formula using recursive function calls

n Ck = (n-1) C (k-1) + (n-1) C k
n C0 = 1
n Cn = 1

Read two user input n and k and report all combinations calculated in the process. 

For example, if user input n = 3 and k = 1

3C1 = 2C0 + 2C1 
2C0 = 1
2C1 = 1C0 + 1C1
1C0 = 1
1C1 = 1
2C1 = 2
3C1 = 3

 If user input n = 4 and k = 2

4C2 = 3C1 + 3C2
3C1 = 2C0 + 2C1 
2C0 = 1
2C1 = 1C0 + 1C1
1C0 = 1
1C1 = 1
2C1 = 2
3C1 = 3
3C2 = 2C1 + 2C2
2C1 = 1C0 + 1C1
1C0 = 1
1C1 = 1
2C1 = 2
2C2 = 1
3C2 = 3
4C2 = 6

If user input n = 5 and k = 5

5C5 = 1
'''
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
