"""
kata link: https://www.codewars.com/kata/54e6533c92449cc251001667  
Instruction : Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.


Code:"""
def unique_in_order(iterable):
    prev = None
    lst = []
    for element in iterable:
        if element != prev:
            lst.append(element)
            prev = element
    return lst
        