class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Use backtrack to get all possible permutations of s1 as a list

        Then iterate through s2 to match the correct one 


        """

        perm_list = []

        def backtrack(i, s1_copy):
            if i >= len(s1):
                perm_list.append(s1_copy)
                return 

            for j in range(i, len(s1_copy)):
                s1_copy[i], s1_copy[j] = s1_copy[j], s1_copy[i]
                backtrack(i + 1, s1_copy)
                
                s1_copy[i], s1_copy[j] = s1_copy[j], s1_copy[i]


            return 

        backtrack(0, s1.copy())


        

            