class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left,right):
            count = 0
            while left >=0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count 
        
        total_count = 0
        for i in range(len(s)):
            total_count += expandAroundCenter(i,i)
            total_count += expandAroundCenter(i-1,i+1)
        return total_count
        
        