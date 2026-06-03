class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l = 1
        r = len(nums) - 1
        i=0
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            l = i+1
            r = len(nums) - 1
            target = -1 * nums[i]
            while(l<r):

                if nums[l] + nums[r] > target:
                    r -=1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l+=1
                    r-=1
                    while (nums[l]== nums[l-1] and l<r):
                        l +=1
        return res
            