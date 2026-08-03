class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp = {}
        for i in range(0,len(nums)):
            comp = target - nums[i]
            if comp in mpp:
                return [mpp[comp],i]
            mpp[nums[i]] = i
        return []
        