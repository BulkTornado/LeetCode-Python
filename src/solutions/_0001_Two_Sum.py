from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 2) and (nums[0] == nums[1]):
            return [0, 1]

        for idx_1, i in enumerate(nums):
            for idx_2, j in enumerate(nums):
                if idx_1 == idx_2:
                    pass
                if (i != j) and (i + j == target):
                    return [idx_1, idx_2]

        # If no valid pair is found, return an empty list
        return []