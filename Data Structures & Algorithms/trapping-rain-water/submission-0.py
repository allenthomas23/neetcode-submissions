class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                continue
            maxLeft[i] = max(height[i-1], maxLeft[i-1])
        for i in range(len(height)-1,0,-1):
            if i == len(height)-1:
                continue
            maxRight[i] = max(height[i+1], maxRight[i+1])
        l = 0
        r = len(height)-1
        water = 0
        for i in range(len(height)):
            water += max(min(maxRight[i],maxLeft[i]) - height[i],0)
        return water