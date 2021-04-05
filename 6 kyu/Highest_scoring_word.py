#kata link: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272  
#Instruction : Given a string of words, you need to find the highest scoring word.
#Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
#You need to return the highest scoring word as a string.
#If two words score the same, return the word that appears earliest in the original string.
#All letters will be lowercase and all inputs will be valid.

#Code:
def high(x):
    def points(i):
        word_count = 0
        for letter in i:
            word_count += ord(letter) - (ord("a")-1)
        return word_count
    sentence_split = x.split()
    points_list = []
    for word in sentence_split:
        points_list.append(points(word))
    max_index = points_list.index(max(points_list))
        
    return sentence_split[max_index]