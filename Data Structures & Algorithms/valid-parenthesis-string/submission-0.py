class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        get all parentheses

        set the number of stars aside

        check the parenthesis list with a stack

        if missing then discount them from number of stars

        return true if the stack is solved (empty)

        Input: s = "((**)"

        p_list = [(, (, )]
        star_num = 1

        stack = [  ]


        """

        p_list = []
        star_num = 0
        for ch in s:
            if ch != "*":
                p_list.append(ch)
            else:
                star_num += 1

        stack = []
        for p in p_list:
            if stack and stack[-1] == "(" and p == ")":
                stack.pop()
            else:
                stack.append(p)

        while len(stack) > 0 and star_num > 0:
            stack.pop()
            star_num -= 1

        return True if len(stack) == 0 else False



        