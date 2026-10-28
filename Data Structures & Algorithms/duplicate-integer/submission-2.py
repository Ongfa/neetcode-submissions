class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        left = 0
        right = 1
        n = len(nums)
        nums.sort()
        while left <= right and left < n and right < n:
            if nums[left] == nums[right]:
                return True
            left += 1
            right += 1

        return False