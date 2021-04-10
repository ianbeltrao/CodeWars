"""
kata link: https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991  
Instruction : The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. 
Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".

Code:"""

def revrot(strng, sz):
    if len(strng) < sz or len(strng) == 0 or sz <= 0:
        return ""
    chunks = []
    output = []
    cubes = 0
    modified_chunk = ""
    while len(strng) >= sz:
        chunks.append(strng[:sz])
        strng= strng[sz:]
    for chunk in chunks:
        for number in chunk:
            number = int(number)
            cubes += number**3
        if cubes % 2 == 0:
            output.append(chunk[::-1])
        else:
            modified_chunk = chunk
            modified_chunk += chunk[0]
            modified_chunk = modified_chunk[1:]
            output.append(modified_chunk)
        cubes = 0
    return "".join(output)
            