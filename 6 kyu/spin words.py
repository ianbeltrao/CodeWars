def spin_words(sentence):
    word_lst = sentence.split()
    for i in range(len(word_lst)):
        if len(word_lst[i])>4:
            word_lst[i] = word_lst[i][::-1]
    
    return " ".join(word_lst)
