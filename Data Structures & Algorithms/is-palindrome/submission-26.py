class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [char for char in s.replace(" ", "").lower() if char.isalnum()]
        print(s)

        j = 0
        k = len(s) - 1
        while j < k:
            print(j, k)
            print(s[j], s[k])
            if s[j] == s[k]:
                j += 1
                k -= 1
            else:
                return False

        return True