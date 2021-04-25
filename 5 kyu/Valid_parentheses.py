"""
kata link: https://www.codewars.com/kata/52774a314c2333f0a7000688  
Instruction : Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, and false if it's invalid.

Code:"""
def valid_parentheses(string):
    check = 0
    for c in string:
        if c == "(":
            check += 1
        if c == ")":
            check -= 1
        if counter < 0:
            return False
    return check == 0

    