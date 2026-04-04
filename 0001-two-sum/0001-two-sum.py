class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        current_sum = 0
        for start in range(n):
            for end in range(start + 1, n):
                sum = nums[start] + nums[end]
                if sum == target:
                    return [start, end]
