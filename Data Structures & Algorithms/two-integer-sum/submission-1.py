class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1 = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in map1:
                map1[nums[i]] = i
            else:
                return [map1[diff],i]