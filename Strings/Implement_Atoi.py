class Solution:
    def atoi(self, s):
        if not s:
            return -1
    
        # Check for negative sign
        negative = False
        if s[0] == '-':
            negative = True
            s = s[1:]
    
        # Iterate through the string and check for non-digit characters
        for char in s:
            if not char.isdigit():
                return -1
    
        # Convert the string to an integer
        num = 0
        for char in s:
            num = num * 10 + int(char)
    
        # Apply negative sign if necessary
        if negative:
            num = -num
    
        return num