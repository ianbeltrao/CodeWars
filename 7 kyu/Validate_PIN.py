#kata link: https://www.codewars.com/kata/55f8a9c06c018a0d6e000132  
#Instruction : ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
#If the function is passed a valid PIN string, return true, else return false.

#Code:
def validate_pin(pin):
    for num in pin:
        if num.isdigit() == False:
            return False
    if len(pin) == 4:
        return True
    if len(pin) == 6:
        return True
    else: 
        return False