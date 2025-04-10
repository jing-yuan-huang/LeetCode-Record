from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_set = set(nums)
        long_streak = 0
        for num in nums_set :
            if (num - 1) not in nums_set :
                current_num = num
                current_streak = 1
                while (current_num + 1 ) in nums_set:
                    current_num += 1
                    current_streak += 1
                long_streak = max(long_streak,current_streak)
        return long_streak
            