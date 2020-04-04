class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        
        for i in range(len(nums) - 1, -1, -1):
            if i > 0 and nums[i-1] < nums[i]:
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[i-1] < nums[j]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                break

        nums[i:] = nums[i:][::-1]
        return nums
            
