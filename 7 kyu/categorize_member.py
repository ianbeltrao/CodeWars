#kata link: https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa  
#Instruction : Categorize the inputs given and return the category. Check the link for a better explanation.

#Code:
def open_or_senior(members):
    member_categories = []
    for member in members:
        if member[0] >= 55 and member[1] > 7:
            member_categories.append("Senior")
        else:
            member_categories.append("Open")
    return member_categories