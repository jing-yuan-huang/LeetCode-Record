from typing import List 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [ ]
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1] :
                continue

            right = len(nums) - 1 
            left =  i+1
            while left < right :
                if nums[i] + nums[left] + nums[right] == 0 :
                    result.append([nums[i], nums[left], nums[right]])
                    left = left + 1
                    right = right -1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right]  > 0 :
                    right = right - 1
                elif nums[i] + nums[left] + nums[right] < 0 :
                    left = left + 1
        return result
            

                

        