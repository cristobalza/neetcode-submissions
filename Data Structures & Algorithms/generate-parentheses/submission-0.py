class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(open_p, close_p, subset):
            if open_p == close_p == n:
                res.append("".join(subset.copy()))
                return

            if open_p < n:
                subset.append("(")
                backtrack(open_p + 1, close_p, subset)
                subset.pop()

            if close_p < open_p:
                subset.append(")")
                backtrack(open_p, close_p + 1, subset)
                subset.pop()

            return 

        backtrack(0, 0, [])

        return res