class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        votes = [True]*len(senate)
        r, d = 0, 0
        rv, dv = 0, 0
        for v in senate:
            if v == "R":
                rv += 1
            else:
                dv += 1
        while rv and dv:
            for i in range(len(senate)):
                if not votes[i]:
                    continue
                if senate[i] == "R" and d:
                    d -= 1
                    votes[i] = False
                    rv -= 1
                elif senate[i] == "D" and r:
                    r -= 1
                    votes[i] = False
                    dv -= 1
                elif senate[i] == "R":
                    r += 1
                else:
                    d += 1
        if rv:
            return "Radiant"
        return "Dire"
            

