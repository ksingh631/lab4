#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_string):
    """Return the first five characters of the input string."""
    return input_string[:5]

def last_seven(input_string):
    """Return the last seven characters of the input string."""
    return input_string[-7:]

def middle_number(input_number):
    """Return the second and third characters of the input number as a string."""
    return str(input_number)[1:3]

def first_three_last_three(arg1, arg2):
    """Return a string starting with the first three characters of arg1 and ending with the last three characters of arg2."""
    return arg1[:3] + arg2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
