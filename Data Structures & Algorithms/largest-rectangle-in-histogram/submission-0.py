class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxR = 0
        stack = []

        for i, height in enumerate(heights):
            start =  i
            while(stack and stack[-1][1] > height):
                index, h =  stack.pop()
                maxR = max(maxR, h * (i-index))
                start = index
            stack.append((start,height))

        for i, h in stack:
            maxR = max(maxR, h * (len(heights) - i))
        return maxR
