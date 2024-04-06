#153. Find Minimum in Rotated Sorted Array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        res=nums[0]
        r=len(nums)-1
        while l<=r:
            if nums[l]<nums[r]:
                res=min(nums[l],res)
                break
            mid=(l+r)//2
            res=min(res,nums[mid])
            if nums[l]<=nums[mid]:
                l=mid+1
            else:
                r=mid-1
        return res
