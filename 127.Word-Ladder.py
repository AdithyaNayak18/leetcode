class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset=set(wordList)
        if endWord not in wordset:
            return 0
        queue=deque()
        queue.append((beginWord,1))
        while len(queue)!=0:
            currword,level=queue.popleft()
            if currword==endWord:
                return level
            for i in range(0,len(currword)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c==currword[i]:
                        continue
                    newword=currword[:i]+c+currword[i+1:]
                    if newword in wordset:
                        queue.append((newword,level+1))
                        wordset.remove(newword)
        return 0
