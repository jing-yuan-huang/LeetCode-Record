from collections import Counter 
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = Counter (s)
        res = 0
        odd_found = False
        for c in seen.values() :
            res += (c // 2 )*2 
            if c % 2 == 1 :
                odd_found = True
        if odd_found :
            res += 1
        return  res
"""
原始長度 - 無法配對的奇數字元數量 + 1（那個 +1 是中間字元）。
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_freq_chars_count = 0
        frequency_map = {}

        for c in s:
            frequency_map[c] = frequency_map.get(c, 0) + 1
            if frequency_map[c] % 2 == 1:
                odd_freq_chars_count += 1
            else:
                odd_freq_chars_count -= 1

        if odd_freq_chars_count > 0:
            return len(s) - odd_freq_chars_count + 1
        else:
            return len(s)
"""