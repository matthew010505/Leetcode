#2958. Length of Longest Subarray With at Most K Frequency
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l=0
        maxi=1
        freq=defaultdict(int)
        for r in range(len(nums)):
            freq[nums[r]]+=1
            while freq[nums[r]]>k:
                freq[nums[l]]-=1
                l+=1
            maxi=max(maxi,r-l+1)
        return maxi
#sliding window
