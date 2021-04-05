#kata link: https://www.codewars.com/kata/52efefcbcdf57161d4000091  
#Instruction : The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#What if the string is empty? Then the result should be empty object literal, {}.

#Code:
def count(string):
    list_keys = []
    list_values = []
    for letter in string:
        if list_keys.count(letter) < 1:
            list_keys.append(letter)
    for letter in list_keys:
        list_values.append(string.count(letter))
    return dict(zip(list_keys, list_values))