from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_size = 0
        left = 0
        right = len(height)-1

        while left < right:
            size = min(height[left],height[right]) * (right - left)
            max_size = max(max_size,size)
            if height[left] < height[right]:
                left += 1
            else :
                right -= 1
        return max_size