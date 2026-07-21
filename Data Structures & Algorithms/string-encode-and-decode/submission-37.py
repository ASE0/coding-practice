class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ''
        for word in strs:
            coded += str(len(word)) + '.' + word
        return coded

    def decode(self, s: str) -> List[str]:
        decoded = []
        c = 0
        j = 0
        for char in s:
            if char == '.':
                decoded.append(s[c + 1:int(s[j:c]) + c + 1])
                j += int(s[j:c]) + int(len(s[j:c])) + 1
            c += 1
        return decoded

        
