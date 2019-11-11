class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        shortest_k = k % len(nums)
        if shortest_k != 0:
            # when use the function itself, "self" is necessary
            self.reverse(nums, 0, len(nums) - 1)
            self.reverse(nums, 0, shortest_k - 1)
            self.reverse(nums, shortest_k, len(nums) - 1)
    def reverse(self, nums: List[int], start: int, end: int ) -> None:
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start = start + 1
            end = end - 1