"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


from typing import List


class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            missing_amount = target - nums[i]
            if missing_amount in hashmap:
                return [hashmap[missing_amount], i]
            hashmap[nums[i]] = i
        return[]


result = Solution2.twoSum(Solution2, [2, 7, 11, 15], 9)
print(result)

result = Solution2.twoSum(Solution2, [3, 2, 4], 6)
print(result)

result = Solution2.twoSum(Solution2, [3, 3], 6)
print(result)
