class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        shortest_k = k % len(nums)
        if shortest_k != 0:
            temp = []
            point = len(nums) - shortest_k
            for i in range(point):
                temp.append(nums[i])
            # rotate from the right to left
            for j in range(point, len(nums)):
                nums[j-point] = nums[j]
            # fill out the first taken out number
            for i, j in zip(range(point), range(shortest_k, len(nums))):
                nums[j] = temp[i]
