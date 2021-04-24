"""
kata link: https://www.codewars.com/kata/520b9d2ad5c005041100000f  
Instruction : Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
#Leave punctuation marks untouched.

Code:"""
def pig_it(text):
    split = text.split()
    lst = []
    word_mod = ""
    for word in split:
        if word.isalpha():
            word_mod += word[1:] + word[0] + "ay"
            lst.append(word_mod)
        else:
            lst.append(word)
        word_mod = ""
    return " ".join(lst)


