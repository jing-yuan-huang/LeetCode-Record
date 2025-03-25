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