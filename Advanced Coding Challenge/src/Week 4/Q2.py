# 2. Roman Numerals
# Problem Description

# Roman numerals are a numeral system that originated in ancient Rome. Numbers in this system are represented by combinations of letters from the Latin alphabet.

# Symbol    I    V     X     L     C      D      M

# Value     1    5     10    50    100    500    1000
# Roman numerals are usually written from largest to smallest from left to right. For example, 2 is marked as II and 7  is marked as VII . However, there are some special cases like : 4  is written as IV and 9 is written as IX . The current year (2021) can be noted as MMXXI .

# You can find more about roman numerals on Wikipedia.

# You will be given a roman numeral and translate it into an Arabic numeral. 

# Sample Input/Output

# Case 1

# Input

# MMXXI
# Output

# 2021
# Case 2

# Input

# XII
# Output

# 12
# Case 3

# Input

# IX
# Output

# 9
def roman_translate(num):

    ##dictionary for roman numbers
    roman_to_number = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    ##list of roman numbers converted to int
    number_sum_list = []
    for i in num:
        number_sum_list.append(roman_to_number[i])

    ## count the output
    ## if the previous number is smaller than the next number, minus it
    ## else add it
    output = 0
    for i in range(len(number_sum_list) - 1):
        if number_sum_list[i] < number_sum_list[i + 1]:
            output -= number_sum_list[i]
        else:
            output += number_sum_list[i]

    ## add the last digit because it havent been looped
    output += number_sum_list[-1]
    
    return output

def main():

    num = input()
    print(roman_translate(num))

main()