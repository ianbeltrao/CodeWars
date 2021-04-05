#kata link: https://www.codewars.com/kata/586538146b56991861000293  
#Instruction : You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

#Code:
def to_nato(words):
    
    dictionary = {'A':'Alfa', 
                  'B':'Bravo',
                  'C':'Charlie', 
                  'D':'Delta', 
                  'E':'Echo', 
                  'F':'Foxtrot', 
                  'G':'Golf',
                  'H':'Hotel',
                  'I':'India', 
                  'J':'Juliett', 
                  'K':'Kilo', 
                  'L':'Lima', 
                  'M':'Mike', 
                  'N':'November', 
                  'O':'Oscar', 
                  'P':'Papa', 
                  'Q':'Quebec', 
                  'R':'Romeo', 
                  'S':'Sierra', 
                  'T':'Tango', 
                  'U':'Uniform', 
                  'V':'Victor', 
                  'W':'Whiskey', 
                  'X':'Xray', 
                  'Y':'Yankee', 
                  'Z':'Zulu',
                  '.': '.',
                  '!': '!',
                  '?': '?'}
    sentence = []
    words_split = words.upper().split()
    for word in words_split:
        for letter in word:
            sentence.append(dictionary.get(letter))
    return " ".join(sentence)