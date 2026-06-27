class Solution:
    def decodeString(self, s: str) -> str:
        res = ""
        i = 0
        while i <= len(s)-1:
            if 0 <= ord(s[i])-ord('a') <= 26:
                res += s[i]
                i += 1
            elif s[i] in "0123456789":
                k = ""
                while s[i] in "0123456789":
                    k += s[i]
                    i += 1
                start = i
                brackets = 1
                i += 1
                while brackets != 0:
                    if s[i] == ']':
                        brackets -= 1
                    if s[i] == '[':
                        brackets += 1
                    i += 1
                end = i
                for _ in range(int(k)):
                    res += self.decodeString(s[start+1:end-1])
        return res