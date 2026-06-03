class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        largest = 0
        filter = set()
        for num in nums:
            filter.add(num)
        sortedList = sorted(filter)
        for num in sortedList:
            if num+1 in nums:
                count +=1
            else:
                largest = max(count, largest)
                count = 1
        return largest