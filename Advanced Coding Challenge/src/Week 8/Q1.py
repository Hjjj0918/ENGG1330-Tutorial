'''
Card Deck
Problem Description

Consider the following two lines of python code.

import itertools, random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
Find out what the code does. Try to explain to yourself what is going on? You may check the Python documentation to figure it out.

Helpful Links:

https://docs.python.org/3/library/itertools.html

https://docs.python.org/3/library/random.html

Write a Python program that will output a list of 50 random cards drawn with replacement from the deck. This time no need to handwrite your solution first. You can directly start coding on ed.

Hint: Use only a single additional line of code to do this. 

There is no auto grader for this one. Ask your student TA if your code is correct.
'''

import itertools, random
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club'])) # Cartisesian Product
#print(deck)
print(random.choices(deck, k=50))