import string

class Solution:
    def cleanString(self,s:str) -> str:
        s = s.translate(str.maketrans('','', string.punctuation))
        s = s.replace(" ", "").lower()
        return s
    
    def isPalindrome(self, s: str) -> bool:
        s = self.cleanString(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
       
