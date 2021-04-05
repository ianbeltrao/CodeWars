#kata link: https://www.codewars.com/kata/546f922b54af40e1e90001da  
#Instruction : In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
#"a" = 1, "b" = 2, etc.

#Code:
def alphabet_position(text):
    text_lower = text.lower()
    numbers_text = []
    for letter in text_lower:
        if ord(letter) >= ord("a") and ord(letter) <= ord("z"):
            numbers_text.append(str(ord(letter) - 96))
        else:
            pass
    return " ".join(numbers_text)