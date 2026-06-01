class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS, stringT = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            stringS[s[i]] = 1 + stringS.get(s[i], 0)
            stringT[t[i]] = 1 + stringT.get(t[i], 0)
        for c in stringS:
            if stringS[c] != stringT.get(c, 0):
                return False
        
        return True

