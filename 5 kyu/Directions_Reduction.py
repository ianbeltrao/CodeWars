"""
kata link: https://www.codewars.com/kata/550f22f4d758534c1100025a  
Instruction : Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).

Code:"""
def dirReduc(arr):
    exclude = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    output = []
    for direction in arr:
        if len(output) and exclude[direction] == output[-1]:
            output.pop()
        else:
            output.append(direction)
    return output