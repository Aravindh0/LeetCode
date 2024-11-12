class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        
        # Loop through the list
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        # Return the new length of the list after removing `val`
        return k