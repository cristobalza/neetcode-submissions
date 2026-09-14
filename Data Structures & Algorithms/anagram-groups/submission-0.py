class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = collections.defaultdict(list) # array with characters : list of words from strs

        for word in strs:
            char_list = [0]*26
            for ch in word:
                char_list[ord("a") - ord(ch)] += 1
            hmap[tuple(char_list)].append(word)

        res = []
        for lst in hmap.values():
            res.append(lst)

        return res

    