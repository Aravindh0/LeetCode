class Solution:
    def twoSum(self, nums, target):
        for index1, num1 in enumerate(nums):
            for index2 in range(index1 + 1, len(nums)):
                num2 = nums[index2]
                if num1 + num2 == target:
                    indexes = [index1, index2]
                    break
        return indexes

        