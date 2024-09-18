class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #add open parenthesis only when open<n 
        #all close parenthesis only if close<open
        #valid only iff open=close=n
        stack =[]
        res = []
        def backtrack(openN,closedN):
            if openN == closedN == n:
                res.append("".join(stack))     #appends the elements of stack into result without any commas or gaps between elements
                return

            if openN<n:
                stack.append("(")
                backtrack(openN+1,closedN)
                stack.pop()

            if closedN<openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()

        backtrack(0,0)
        return res


        
