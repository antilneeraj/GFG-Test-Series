class Solution:
    def binarySubstring(self, n, s):
        count = 0
        for i in range(n):
            if s[i] == '1':
                count += 1

        count = count * (count - 1) // 2
        return count