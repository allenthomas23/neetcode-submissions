class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            maxtemp = temperatures[i]
            k=0
            for j in range(i+1,len(temperatures)):
                if maxtemp < temperatures[j]:
                    k = j-i
                    break
            result[i] = k
        return result