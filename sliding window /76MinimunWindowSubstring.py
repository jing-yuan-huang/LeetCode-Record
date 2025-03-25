from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        char_count = Counter(t) # each char in t and its count
        target_char_remiain = len(t) # remaining char in t to be matched
        min_window = (0,float('inf')) 
        left = 0 
        for right in range(len(s)): 

            if char_count[s[right]] > 0 :
                target_char_remiain -= 1  # if the char in s is in t, then decrease the remaining count
            char_count[s[right]] -= 1 
            

            if target_char_remiain == 0:
                while True:
                    if char_count[s[left]] == 0:
                        break
                    char_count[s[left]] += 1
                    left += 1
                if right - left < min_window[1] - min_window[0]:
                    min_window = (left,right)

                char_count[s[left]] += 1
                target_char_remiain += 1
                left += 1
            #如果找到一個符合的就嘗試縮小，不能再縮小了，會先推進一格left 讓right繼續往右找 直到補完所有的t char_count, target_char_remiain == 0
            # 找出每個小的可能

            
        return s[min_window[0]:min_window[1]+1]

                    

            
            