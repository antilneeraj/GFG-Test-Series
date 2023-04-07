def strstr(s,x):
    if not s or not x or len(x) > len(s):
        return -1

    for i in range(len(s) - len(x) + 1):
        if s[i:i + len(x)] == x:
            return i

    return -1