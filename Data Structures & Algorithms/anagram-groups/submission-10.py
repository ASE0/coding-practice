class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for i in strs:
            code = [0] * 26

            for char in i:
                count = ord(char) - ord("a")
                code[count] += 1

            res[tuple(code)].append(i)

        return list(res.values())