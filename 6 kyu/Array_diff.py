#kata link: https://www.codewars.com/kata/523f5d21c841566fde000009  
#Instruction : Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b.
#If a value is present in b, all of its occurrences must be removed from the other:

#Code:
def array_diff(a, b):
    for num in b:
        if a.count(num) > 0:
            try:
                while True:
                    a.remove(num)
            except ValueError:
                pass
    return a