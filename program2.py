class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }
        
        num=0
        i = 0
        n = len(s)
        
        while i < n:
            if i + 1 < n and s[i:i+2] in roman_to_int:
                num += roman_to_int[s[i:i+2]]
                i += 2
            else:
                num += roman_to_int[s[i]]
                i += 1
        
        return num
