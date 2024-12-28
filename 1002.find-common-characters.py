class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for char in set(words[0]):
            count = min(word.count(char) for word in words)
            res += [char] * count
        return res
