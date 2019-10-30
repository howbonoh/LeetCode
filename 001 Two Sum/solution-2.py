class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        for i in range(len(nums)):
            another = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j] == another:
                    flag = True
                    break
            if flag == True:
                break
        return [i,j]