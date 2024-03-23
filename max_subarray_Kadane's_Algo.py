#kadane algorithm Sliding window-pointer approach-53 medium
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=0
        maxsub=nums[0]
        for i in nums:
            if currsum<0:
                currsum=0
            currsum+=i
            maxsub=max(maxsub,currsum)
        return maxsub
