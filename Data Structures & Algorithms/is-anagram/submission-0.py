class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = [0]*26
        t_list = [0]*26

        for ch in s:
            s_list[ord("a") - ord(ch)] += 1
        
        for ch in t:
            t_list[ord("a") - ord(ch)] += 1

        return s_list == t_list