"""
kata link: https://www.codewars.com/kata/5264d2b162488dc400000001  
Instruction : Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (like the name of this kata).

    Strings passed in will consist of only letters and spaces.
    Spaces will be included only when more than one word is present.
Code:"""
def spin_words(sentence):
    word_lst = sentence.split()
    for i in range(len(word_lst)):
        if len(word_lst[i])>4:
            word_lst[i] = word_lst[i][::-1]
    
    return " ".join(word_lst)
