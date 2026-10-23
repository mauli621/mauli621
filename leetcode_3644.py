class Solution:
    def sortPermutation(self, nums):
        n = len(nums)
        k = -1

        for i in range(n):
            if nums[i] != i:
                k = k & nums[i] & i

        if k == -1:
            return 0

        return k