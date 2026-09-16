class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """

                        i= 0
                        1

                    i=1.     
                    2           


        i=2.      i=3
        0.        1


                  i=4
                  true

         0 1 2 3 4
        [1,2,0,1,0]
        

        i = 1
        nums[i] = 1

        2 + 0 = 2



        goal_idx = 3


        """


        goal_idx = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal_idx:
                goal_idx = i

        return goal_idx == 0
        