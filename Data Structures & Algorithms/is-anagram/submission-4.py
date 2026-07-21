class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        for char in s:
            s = s.replace(char, '', 1)
            t = t.replace(char, '', 1)
        print(s)
        print(t)
        if len(s) == len(t):
            return True
        else:
            return False