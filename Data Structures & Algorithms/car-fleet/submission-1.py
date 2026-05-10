class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = [[p, s] for p, s in zip(position, speed)]
        for p, s in sorted(pairs)[::-1]:
            arrival = (target-p)/s
            if not len(stack):
                stack.append(arrival)
            elif arrival > stack[-1]:
                stack.append(arrival)

        return len(stack)

        
                