class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        i = 0
        while i <= furthest and i < len(nums):
            furthest = max(furthest, i + nums[i])
            i += 1
        return furthest >= len(nums) - 1