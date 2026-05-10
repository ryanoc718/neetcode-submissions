class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + "#" + s
        return code

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            wordLength = int(s[i:j])
            i = j + 1
            j = i + wordLength
            results.append(s[i:j])
            i = j
            
        return results


