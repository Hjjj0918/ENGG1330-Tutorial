'''
C(40 marks): Write a python program that stores a random number from 0-99 in a variable named target 
(this part is provided). Note that target will not be further updated in the program.  
 
The program then accepts user input and stores it in a variable named guess. You may assume that the 
user only enters integers. The program ends when guess is equal to target otherwise the program 
continuously asks the user to provide a guess. Output Correct after x trial! when the program ends, 
where x is the number of times the user has provided input. 
 
The program should output a guess range according to the user’s guess value. If user’s guess number is 
out of the guess range, output the error message Not in the range!  
 
Consider the following sample run with bold text representing user input. Suppose target = 12. 
Guess a number 0 - 99 : 50 
Guess a number 0 - 50 : 51 
Not in the range! 
Guess a number 0 - 50 : 30 
Guess a number 0 - 30 : 10 
Guess a number 10 - 30 : 9 
Not in the range! 
Guess a number 10 - 30 : 12 
Correct after 6 trial! 
We provide partial code to you. Please complete it.  
'''
import random 
target = random.randint(0,100) 
min = 0 
max = 99 
print("Guess a number",min,"-",max,": ",end="") 
guess = int(input())
count = 0;
if guess == target:
    count += 1
    print("Correct after",count,"trial!")
else:
    while guess != target:
        count += 1
        if guess < min or guess > max:
            print("Not in the range!")
        else:
            if guess < target:
                min = guess
            else:
                max = guess
        print("Guess a number",min,"-",max,": ",end="")
        guess = int(input())
    count += 1
    print("Correct after",count,"trial!")