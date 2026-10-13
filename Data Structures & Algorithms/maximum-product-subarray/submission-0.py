class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        prefix = float("-inf")
        suffix = 1

        for num in nums:

            suffix *= num 

            prefix = max(prefix, suffix)

            if suffix < 0:
                suffix = 1
        
        return prefix