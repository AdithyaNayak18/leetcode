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


#DSA recursion
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def solve(i,total,brackets,res):
            if i>=len(brackets):
                if total==0:
                    res.append("".join(brackets))
                return
            
            if total>(len(brackets)//2):
                return
            elif total<0:
                return
            
            brackets[i]='('
            sum=total+1
            solve(i+1,sum,brackets,res)
            brackets[i]=')'
            sum=total-1
            solve(i+1,sum,brackets,res)
        brackets=[""]*(n*2)
        res=[]
        solve(0,0,brackets,res)
        return res
        
