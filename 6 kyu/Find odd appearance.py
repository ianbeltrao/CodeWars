def find_it(lst):
    output = []
    for num in lst:
        if lst.count(num) % 2 != 0:
            output.append(num)
    return output[0]