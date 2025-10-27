'''
@ENGG1330: Computer Programming 1
The suggested solution for the Quiz -- Tutorial in Week 8
'''

def Sum(digits:list) -> int:
    return sum(digits)

def product(digits:list) -> int:
    '''There are multiple more efficient third-party methods of obtaining products of ints/floats
    but this works as well'''
    prod = 1
    for digit in digits:
        prod *= digit
    return prod

def subtract(product, Sum):
    # Note that "sum" is a keyword in python
    return product - Sum

def main():
    n = input("Input number:")
    
    # Iterate over the string, "n", type cast it to an intger and append it to the list digits 
    digits = [int(i) for i in n]

    print(
        subtract(
            product(digits),
            Sum(digits)
        )
    )

main()