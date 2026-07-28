class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def twist(code):
            codes = []
            for c in range(len(code)):
                d = int(code[c])
                if d == 9:
                    codes.append(code[:c] + "0" + code[c+1:])
                else:
                    codes.append(code[:c] + str(d+1) + code[c+1:])
                if d == 0:
                    codes.append(code[:c] + "9" + code[c+1:])
                else:
                    codes.append(code[:c] + str(d-1) + code[c+1:])
            return codes
        
        seen = set(deadends)
        if "0000" in seen:
            return -1
        q = deque(["0000"])
        twists = -1
        while q:
            twists += 1
            for _ in range(len(q)):
                code = q.popleft()
                if code == target:
                    return twists
                for c in twist(code):
                    if c not in seen:
                        seen.add(c)
                        q.append(c)
        return -1

                

