#kata link: https://www.codewars.com/kata/5208f99aee097e6552000148  
#Instruction : Complete the solution so that the function will break up camel casing, using a space between words.
#Example: solution("camelCasing")  ==  "camel Casing"

#Code:
def solution(s):
    import re
    word_list = re.findall("[A-Z][^A-Z]*", s)
    index = s.index(word_list[0])
    word_list.insert(0, s[0:index])
    return " ".join(word_list)