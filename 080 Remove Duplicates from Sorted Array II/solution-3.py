class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums == []: return 0
        i = 0
        # check if there are two same number
        check = False
        for j in range(1,len(nums)):
            if nums[i] != nums[j]:
                check = False
                i = i+1
                nums[i] = nums[j]
            else:
                if check == False:
                    check = True
                    i = i+1
                    nums[i] = nums[j]
        return i+1
