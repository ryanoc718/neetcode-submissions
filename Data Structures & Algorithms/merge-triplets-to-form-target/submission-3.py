class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        one, two, three = False, False, False
        for t in triplets:
            if t == target:
                return True
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            if t[0] == target[0]:
                one = True
            if t[1] == target[1]:
                two = True
            if t[2] == target[2]:
                three = True
        return one and two and three
            








            