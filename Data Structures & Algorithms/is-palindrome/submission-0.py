class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ""
        lowerCase = "abcdefghijklmnopqrstuvwxyz"
        for c in s:
            if ord(c)-ord('a') < 26 and ord(c)-ord('a') >= 0:
                cleanStr += c
            if ord(c)-ord('A') < 26 and ord(c)-ord('A') >= 0:
                cleanStr += lowerCase[ord(c)-ord('A')]
            if ord(c)-ord('0') < 10 and ord(c)-ord('0') >= 0:
                cleanStr += c
        
        i, j = 0, len(cleanStr)-1
        while i < j:
            if cleanStr[i] != cleanStr[j]:
                return False
            i += 1
            j -= 1
        return True