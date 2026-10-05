class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                last_t, last_i = stack.pop()

                res[last_i] = i - last_i

            stack.append((t, i))

        return res

        