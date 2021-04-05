#kata link: https://www.codewars.com/kata/550498447451fbbd7600041c  
#Instruction : Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two arrays have the "same" elements, with the same multiplicities. 
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.

#Code:
def comp(array1, array2):
    if array1 == None or array2 == None or len(array1) != len(array2):
        return False
    
    array1.sort(key=abs)
    array2.sort(key=abs)
    
    for number in range(len(array1)):
        num_1 = array1[number]
        num_2 = array2[number]
        if num_2 != num_1**2:
            return False 
    return True