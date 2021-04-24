"""
kata link: https://www.codewars.com/kata/52685f7382004e774f0001f7  
Instruction : Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

Code:"""
def make_readable(seconds):
    output_sec = int(seconds%60) 
    minutes = int(seconds/60)
    output_min = int(minutes%60)
    output_hour = int(minutes/60)
    return f"{output_hour:02d}:{output_min:02d}:{output_sec:02d}"



