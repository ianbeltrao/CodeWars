"""
kata link: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39  
Instruction : This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:

Code:"""
import ast
def zero(x=0): 
    if type(x) == str:
        if x[0] == "/":
            return 0
        if x[0] == "*":
            return 0
        operation = f"0{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 0
    
def one(x=0):
    if type(x) == str:
        if x[0] == "/":
            return int(1 / int(x[-1]))
        if x[0] == "*":
            return int(x[-1])
        operation = f"1{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 1
def two(x=0): 
    if type(x) == str:
        if x[0] == "/":
            return int(2 / int(x[-1]))
        if x[0] == "*":
            return int(2 * int(x[-1]))
        operation = f"2{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 2
def three(x=0): 
    if type(x) == str:
        if x[0] == "/":
            return int(3 / int(x[-1]))
        if x[0] == "*":
            return int(3 * int(x[-1]))
        operation = f"3{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 3
def four(x=0): 
    if type(x) == str:
        if x[0] == "/":
            return int(4 / int(x[-1]))
        if x[0] == "*":
            return int(4 * int(x[-1]))
        operation = f"4{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 4
def five(x=0): 
    if type(x) == str:
        if x[0] == "/":
            return int(5 / int(x[-1]))
        if x[0] == "*":
            return int(5 * int(x[-1]))
        operation = f"5{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 5
def six(x=0): 
    if type(x) == str:
        if x[0] == "/":
            return int(6 / int(x[-1]))
        if x[0] == "*":
            return int(6 * int(x[-1]))
        operation = f"6{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 6
def seven(x=0): 
    if type(x) == str:
        if x[0] == "/":
            return int(7 / int(x[-1]))
        if x[0] == "*":
            return int(7 * int(x[-1]))
        operation = f"7{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 7
def eight(x=0): 
    if type(x) == str:
        if x[0] == "/":
            return int(8 / int(x[-1]))
        if x[0] == "*":
            return int(8 * int(x[-1]))
        operation = f"8{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 8
def nine(x=0): 
    if type(x) == str:
        if x[0] == "/":
            return int(9 / int(x[-1]))
        if x[0] == "*":
            return int(9 * int(x[-1]))
        operation = f"9{x}"
    
        result = ast.literal_eval(operation)
        return int(result)
    else:
        return 9  

def plus(x):
    return f"+{x}"
def minus(x): 
    return f"-{x}"
def times(x): 
    return f"*{x}"
def divided_by(x): 
    return f"/{x}"