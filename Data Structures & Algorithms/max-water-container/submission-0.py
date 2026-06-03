class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxV = 0
        l = 0
        r = len(heights) - 1
        while (l<r):
            volume = (r-l) * min(heights[r], heights[l])
            if maxV < volume:
                maxV = volume
            if heights[l] > heights[r]:
                r -= 1
            else:
                l +=1
        return maxV