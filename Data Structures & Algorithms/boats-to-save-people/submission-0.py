class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        q = deque(people)
        boats = 0
        while q:
            boats += 1
            heavy = q.pop()
            if len(q) and heavy+q[0] <= limit:
                q.popleft()
        return boats


            
