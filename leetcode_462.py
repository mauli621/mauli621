class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            median = (nums[n // 2 - 1] + nums[n // 2]) / 2
        else:
            median = nums[n // 2]
        ans = 0
        for i in nums:
            if i > median:
                ans = ans + (i - median)
            else:
                ans = ans + (median - i)   
        return ans
        