#kata link: https://www.codewars.com/kata/55c45be3b2079eccff00010f  
#Instruction : Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.
#Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).
#If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

#Code:
def find_number(word):
    for letter in word:
        if letter.isdigit():
            return int(letter)

def order(sentence):
    sentence_split = sentence.split()
    sentence_split = sorted(sentence_split, key= find_number)
    sentence_ordered = " ".join(sentence_split)
    return sentence_ordered