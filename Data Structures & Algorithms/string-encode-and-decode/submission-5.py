class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            count = ""
            while s[i] != "#":
                count += s[i]
                i += 1
            res.append(s[i+1: i+1+int(count)])
            i += int(count)+1
        return res
