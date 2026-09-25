class Solution:

    def encode(self, strs: List[str]) -> str:
        lst = []

        for word in strs:
            lst.append(str(len(word)) + "$" + word)

        return "".join(lst)

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0

        while i < len(s):
            j = i
            size_str = ""
            while s[j] != "$":
                size_str += s[j]
                j += 1

            size_int = int(size_str)

            k = j + 1

            word = s[k: k + size_int]

            res.append(word)

            i  = k + size_int

        return res
