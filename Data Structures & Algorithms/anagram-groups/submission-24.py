class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for word in strs:
            code = [0] * 26

            for i in word:
                count = ord(i) - ord("a")
                code[count] += 1
        
            final[tuple(code)].append(word)
        
        return list(final.values())