class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]

        for i in range(len(operations)):
            if operations[i]=='C':
                stack.pop()
            elif operations[i]=='D':
                s=stack[-1]*2
                stack.append(s)
            elif operations[i]=='+':
                s=stack[-1]+stack[-2]
                stack.append(s)
            else:
                stack.append(int(operations[i]))
        
        return sum(stack)
