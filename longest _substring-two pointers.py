#longest substring without repeating characters.-Two pointers-3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s:
            l,r=0,1
            maxval=1
            while r<len(s):
                if len(s[l:r+1])==len(set(s[l:r+1])):
                    val=len(s[l:r+1])
                    maxval=max(maxval,val)
                else:
                    l+=1
                r+=1
            return maxval
        else:
            return 0
            
