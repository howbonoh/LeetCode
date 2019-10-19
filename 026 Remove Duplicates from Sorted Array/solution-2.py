class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    del nums[j]
                else:
                    j = j+1
            i = i+1
        return len(nums)