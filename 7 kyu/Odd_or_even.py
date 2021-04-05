#kata link: https://www.codewars.com/kata/5949481f86420f59480000e7  
#Instruction : Given a list of integers, determine whether the sum of its elements is odd or even.
#Give your answer as a string matching "odd" or "even".
#If the input array is empty consider it as: [0] (array with a zero).

#Code:
def odd_or_even(arr):
    if sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"