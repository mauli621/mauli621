
class Solution:
    def minMoves(self, nums):
        minimum = min(nums)
        total = 0

        for i in range(len(nums)):
            total = total + (nums[i] - minimum)

        return total
