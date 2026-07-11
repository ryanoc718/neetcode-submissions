class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            if a > 0:
                res.append(a)
            else:
                add = True
                while len(res):
                    if abs(a) > res[-1] and res[-1] > 0:
                        res.pop()
                    elif abs(a) < res[-1]:
                        add = False
                        break
                    elif abs(a) == res[-1]:
                        res.pop()
                        add = False
                        break
                    else:
                        break
                if add:
                    res.append(a)
        return res
                        