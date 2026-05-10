class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""        
        tmap = {}
        smap = {}
        for c in t:
            tmap[c] = tmap.get(c, 0)+1
        l = 0
        while l < len(s) and s[l] not in tmap:
            l += 1
        if l == len(s):
            return ""
        if len(t) == 1:
            return t
        smap[s[l]] = 1
        r= l+1
        while r < len(s):
            smap[s[r]] = smap.get(s[r], 0)+1
            if self.valid(smap, tmap):
                break
            r += 1
        if r == len(s) and not self.valid(smap, tmap):
            return ""
        start, end = l, r+1
        while r < len(s):
            smap[s[l]] -= 1
            l += 1
            if l >= len(s):
                break
            if not self.valid(smap, tmap):
                r += 1
                if r < len(s):
                    smap[s[r]] = smap.get(s[r], 0)+1
            else:
                start = l
                end = r+1
        return s[start: end]
        
    def valid(self, s, t):
        for key in t:
            if s.get(key, 0) < t[key]:
                return False
        return True
        