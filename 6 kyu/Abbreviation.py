def abbreviate(s):
    word = ""
    sentence = []
    output = []
    for c in s:
        if c.isalpha():
            word += c
        else:
            sentence.append(word)
            sentence.append(c)
            word = ""
    sentence.append(word)
    for word in sentence:
        l = len(word)
        if l >= 4:
            output.append(word[0] + str(l - 2) + word[l - 1])
        else:
            output.append(word)
    return "".join(output)