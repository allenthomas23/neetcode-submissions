class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        l,r = 1,max(piles)
        ans = r
        while(l<=r):
            mid = (l+r)//2
            cost =0
            for pile in piles:
                cost += math.ceil(pile/mid)
            if cost <= h:
                ans = mid
                r= mid -1
            elif cost > h:
                l = mid+1

        return ans