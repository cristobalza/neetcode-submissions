class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tuple_list = [(p, s) for p, s in zip(position, speed)]

        tuple_list.sort(key= lambda x: x[0], reverse=True)

        stack = []

        for p, s in tuple_list:

            stack.append((target - p) / s)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)