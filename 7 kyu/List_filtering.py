#kata link: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd  
#Instruction : In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

#Code:
def filter_list(l):
    new_list =[]
    for element in l:
        if type(element) == int:
            new_list.append(element)
    return new_list