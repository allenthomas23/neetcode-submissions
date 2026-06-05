class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        freqt = {}
        freqs = {}
        have = 0
        if t == "" :return ""
        res = [-1,-1]
        resLen = float('infinity')
        for c in t:
            freqt[c] = freqt.get(c,0)+1
        need = len(freqt)
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r],0) + 1
            if s[r] in freqt and freqs[s[r]]==freqt[s[r]]:
                have+=1
    
            while(have ==need):
                if(r-l+1 < resLen):
                    resLen = r-l+1
                    res = [l,r]
                freqs[s[l]] -=1
                if s[l] in freqt and freqs[s[l]] < freqt[s[l]]:
                    have -=1
                l+=1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else""