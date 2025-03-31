from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i , num in enumerate (nums):
            complement = target - num
            if complement in hash_map :
                return [ hash_map[complement],i]
            hash_map[num] = i



"""
for i in range(len(nums)) :
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
"""