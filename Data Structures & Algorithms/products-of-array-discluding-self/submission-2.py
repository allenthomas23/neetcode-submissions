class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod= 1
        output = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    prod *= nums[j]
            output[i] = prod
            prod = 1
        return output
                