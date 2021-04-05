#kata link: https://www.codewars.com/kata/54ff3102c1bad923760001f3  
#Instruction : Return the number (count) of vowels in the given string.
#We will consider a, e, i, o, u as vowels for this Kata (but not y).
#The input string will only consist of lower case letters and/or spaces.

#Code:
def get_count(input_str):
    num_vowels = 0
    vowel = ["a", "e", "i", "o", "u"]
    for letter in input_str:
        if vowel.count(letter) > 0:
            num_vowels += 1
    
    return num_vowels