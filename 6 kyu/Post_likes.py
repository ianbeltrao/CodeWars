#kata link: https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa  
#Instruction : Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item.

#Code:
def likes(names):
    if len(names) == 0:
        return "no one likes this"
    elif len(names) == 1:
        return f"{names[0]} likes this"
    elif len(names) == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif len(names) == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2]) 
    else:
        return"{}, {} and {} others like this".format(names[0], names[1], len(names)-2)
        