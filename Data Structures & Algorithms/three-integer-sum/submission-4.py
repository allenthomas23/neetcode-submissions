class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new = sorted(nums)
        res = list()
        for i in range(len(new)):
            if i > 0 and new[i] == new[i-1]:
                continue
            l,r = i+1, len(new)-1
            while l<r:
                threeSum = new[i] + new[l] + new[r]
                if threeSum > 0:
                    r-=1
                if threeSum < 0:
                    l+=1
                if threeSum == 0:
                    res.append([new[i],new[l], new[r]])
                    l+=1
                    r-=1
                    while l<r and new[l] == new[l-1]:
                        l+=1
                    
        return res
            
            
