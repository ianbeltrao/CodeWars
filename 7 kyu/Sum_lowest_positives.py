#kata link: https://www.codewars.com/kata/558fc85d8fd1938afb000014  
#Instruction : Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
#For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7

#Code:
def sum_two_smallest_numbers(numbers):
    lowest = min(numbers)
    numbers.remove(lowest)
    return lowest+min(numbers)