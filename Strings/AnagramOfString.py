def remAnagram(S1,S2):
    freq1 = {}
    freq2 = {}

    for char in S1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    for char in S2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    total_chars_to_delete = 0

    for char in freq1.keys():
        if char in freq2:

            total_chars_to_delete += abs(freq1[char] - freq2[char])
        else:

            total_chars_to_delete += freq1[char]

    for char in freq2.keys():
        if char not in freq1:
            total_chars_to_delete += freq2[char]

    return total_chars_to_delete