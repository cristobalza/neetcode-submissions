class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        Look at position of the p or stars not the actual symbol
        -> use index instead

        iterate through the s

            if star -> append to a start stack idx!

            elif a open p -> append to p stack idx!

            else (close p)
                check if p stack and star stack non empty
                    return False if true above

                if open p stack -> pop

                else star stack -> pop

            EDGE CASE
            
            if any of the idx in higher in p stack then return False


        """

        star_stack = []
        p_stack = []

        for i, ch in enumerate(s):
            if ch == "*":
                star_stack.append(i)

            elif ch == "(":
                p_stack.append(i)

            else:
                if not p_stack and not star_stack:
                    return False
                
                elif p_stack:
                    p_stack.pop()

                else:
                    star_stack.pop()

        while p_stack and star_stack:
            if p_stack.pop() > star_stack.pop():
                return False

        return True if len(p_stack) == 0 else False




        