#kata link: https://www.codewars.com/kata/5259b20d6021e9e14c0010d4  
#Instruction : Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

#Code:
def reverse_words(text):
    string_list = text.split(" ")
    new_list = [word[::-1] for word in string_list]
    
    return " ".join(new_list)