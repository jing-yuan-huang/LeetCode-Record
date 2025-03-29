class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_list = []
        maxlen = 0
        for char in s :
            if char in count_list:
                idx = count_list.index(char)
                count_list = count_list [idx+1:]
            count_list.append(char)
            currentlen = len (count_list)
            maxlen = max (maxlen,currentlen)
        return maxlen

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_str = set ()
        left = 0
        count = 0 
        for right in range(len(s)) :
            while s[right] in res_str:
                res_str.remove(s[left])
                left += 1
            res_str.add(s[right])
            count = max(count, right - left + 1)
        return count
"""