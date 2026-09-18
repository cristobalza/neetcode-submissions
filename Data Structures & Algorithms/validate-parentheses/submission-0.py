class Solution:
    def isValid(self, s: str) -> bool:

        res = []

        hmap = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        for ch in s:

            if ch in hmap:
                res.append(ch)
            else:
                if not res:
                    return False

                open_p = res.pop()

                if hmap[open_p] != ch:
                    return False

        return True if len(res) == 0 else False    