#kata link: https://www.codewars.com/kata/57f609022f4d534f05000024  
#Instruction : You are given an odd-length array of integers, in which all of them are the same, except for one single number.
#Complete the method which accepts such an array, and returns that single different number.
#The input array will always be valid! (odd-length >= 3)

#Code:
def stray(arr):
    for number in arr:
        if arr.count(number) == 1:
            return number