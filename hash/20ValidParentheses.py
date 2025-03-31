class Solution:
    def isValid(self, s: str) -> bool:
       char_map = { ")":"(", "]":"[","}":"{"}
       stack = []

       for char in s :
           if char in char_map.values():
               stack.append(char)
           elif char in char_map.keys():
               if stack :
                    top_element = stack.pop()
                    if char_map[char] != top_element:
                        return False
               else :
                   return False
           else:
               return False
       return len(stack) == 0