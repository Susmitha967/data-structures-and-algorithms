class Solution:
    def timeRequiredToBuy(self, nums: List[int], k: int) -> int:
        m = 0
        for i in range(0,len(nums)):
            if i <= k:
                m += min(nums[i],nums[k])
            else:
                m += min(nums[i],nums[k]-1)
        return m
        