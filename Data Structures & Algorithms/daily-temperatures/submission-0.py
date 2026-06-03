class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res =[0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            count = 0
            for j,t in enumerate(temperatures):
                if j>i and t > temp:
                    count = j-i
                    res[i] = count
                    break
            
        return res