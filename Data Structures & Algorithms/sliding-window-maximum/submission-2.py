class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = list()
        maxn = nums[0]
        for r in range(k-1,len(nums)):
            window = nums[l:r+1]
            maxn = window[0]
            for num in window:
                maxn = max(maxn,num)
            res.append(maxn)
            l+=1
        return res
            
