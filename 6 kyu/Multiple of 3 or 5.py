def solution(number):
    num_list = []
    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            num_list.append(num)

    return sum(num_list)