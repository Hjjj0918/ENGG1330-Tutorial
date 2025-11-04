'''
Implement the Ackermann function. 

Get input number m and n from the user and print the result.
'''
def A(m, n):
    if m < 0 or n < 0:
        return 0

    if m == 0:
        return n + 1
    
    if n == 0:
        return A(m - 1, 1)

    return A(m - 1, A(m, n-1))

print(A(int(input()),int(input())))