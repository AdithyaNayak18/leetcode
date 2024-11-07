class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        newPath = path.split('/')
        for c in newPath:
            if c == '..':
                if stack:
                    stack.pop()
            elif c != '' and c != '.':
                stack.append(c)
        return '/' + '/'.join(stack)
