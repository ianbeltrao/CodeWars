#kata link: https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004  
#Instruction : Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

#Code:
def highest_rank(arr):
    arr.sort()
    reversed_arr = arr[::-1]
    counter = 0
    for num in reversed_arr:
        if reversed_arr.count(num) > counter:
            counter = reversed_arr.count(num)
            number = num
    return number