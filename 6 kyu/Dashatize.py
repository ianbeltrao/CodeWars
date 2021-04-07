"""
kata link: https://www.codewars.com/kata/58223370aef9fc03fd000071  
Instruction : Given a variable n,

If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.

If n is not an integer, return an empty value.

Code:"""
def dashatize(n):
    if type(n) != int:
        return "None"
    n = str(n).replace("-", "")
    new_str = ""
    try:
        for num in str(n):
            if abs(int(num)) % 2 == 0:
                new_str += str(num)
            else:
                new_str += f"-{num}-"
    except ValueError:
        return str(n).replace("-", "")
    replaced = new_str.replace("--", "-")
    if replaced[0] == "-":
        replaced = replaced[1::]
    if replaced[-1] == "-":
        replaced = replaced[:-1]
    return replaced