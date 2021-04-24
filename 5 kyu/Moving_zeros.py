"""
kata link: https://www.codewars.com/kata/52597aa56021e91c93000cb0  
Instruction : Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

Code:"""
def move_zeros(array):
    output = []
    for num in array:
        if num != 0:
            output.append(num)
    for i in range(array.count(0)):
        output.append(0)
    return output