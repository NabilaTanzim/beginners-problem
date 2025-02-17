def find_max(num):
    max = num[0]
    for i in num:
        if i > max:
            max = i
    return max