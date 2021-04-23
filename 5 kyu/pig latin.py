def pig_it(text):
    split = text.split()
    lst = []
    word_mod = ""
    for word in split:
        if word.isalpha():
            word_mod += word[1:] + word[0] + "ay"
            lst.append(word_mod)
        else:
            lst.append(word)
        word_mod = ""
    return " ".join(lst)


