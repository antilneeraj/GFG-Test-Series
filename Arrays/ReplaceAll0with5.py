def convertFive(n):
    lst = list(str(n))
    for i in range(len(lst)):
        if lst[i] == '0':
            lst[i] = '5'
    return ''.join(lst)