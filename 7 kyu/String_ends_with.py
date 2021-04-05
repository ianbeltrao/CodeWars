#kata link: https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d  
#Instruction : Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

#Code:
def solution(string, ending):
    len_ending = len(ending)
    if ending in string[-len_ending:]:
        return True
    return False