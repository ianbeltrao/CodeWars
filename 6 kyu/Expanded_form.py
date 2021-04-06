"""
kata link: https://www.codewars.com/kata/5842df8ccbd22792a4000245  
Instruction : You will be given a number and you will need to return it as a string in Expanded Form


Code:"""
def expanded_form(num):
    result = []
    
    for index, value in enumerate(str(num)[::-1]):
        if int(value) != 0:
            result.append(value + ("0"*index))
            
    return " + ".join(result[::-1]) 