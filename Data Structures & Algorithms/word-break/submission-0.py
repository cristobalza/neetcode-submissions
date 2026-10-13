class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """

                    Input: s = "neetcode"
                                    i

                    n.                     c

                neet or code         neet or code

                eet

                et

                t

                ""



                            0123456789
                Input: s = "catsincars"
                                i

                "cats","cat","sin","in","car"


                ats , at ar.     

                ts  t 

                s



                ""


               set("cats","cat","sin","in","car")


               "catsincars"
                i

                    j 

        """
        hset = set()

        for word in wordDict:
            hset.add(word)

        def dfs(i):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                if s[i: j + 1] in hset:
                    if dfs(j + 1):
                        return True
            return False

        return dfs(0)



        
