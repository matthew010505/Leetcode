class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,total=0,0
        result=len(nums)+2
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                result=min(result,r-l+1)
                total-=nums[l]
                l+=1
        if result==len(nums)+2:
            return 0
        else:
            return result
#209. Minimum Size Subarray Sum
