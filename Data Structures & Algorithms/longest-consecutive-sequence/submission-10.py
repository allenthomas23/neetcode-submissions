class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest = 0
        filter = set(nums)
        for num in filter:
            if (num-1) not in filter:
                count = 1
                while (num + count) in filter:
                    count +=1
                largest= max(count,largest)
                count = 1
        return largest