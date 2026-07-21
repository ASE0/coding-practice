class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final = defaultdict(list)

        for word in strs:
            final[''.join(sorted(word))].append(word)
        
        return list(final.values())