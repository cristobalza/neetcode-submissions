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

                0123456789
               "catsincars"
                i

                    j 

                

        """
        hset = set()

        for word in wordDict:
            hset.add(word)

        memo = {}

        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for j in range(i, len(s)):
                if s[i: j + 1] in hset:
                    if dfs(j + 1):
                        memo[i] = True
                        return memo[i]

            memo[i] = False
            return False

        return dfs(0)



        
