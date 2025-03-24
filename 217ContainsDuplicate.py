from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check_list = set()
        for num in nums:
            if num in check_list:
                return True
            else: check_list.add(num)
        return False

""" 
another solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
"""
