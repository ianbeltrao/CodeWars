def valid_parentheses(string):
    check = 0
    for c in string:
        if c == "(":
            check += 1
        if c == ")":
            check -= 1
        if counter < 0:
            return False
    return check == 0

    