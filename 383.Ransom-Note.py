class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote)>len(magazine):
            return False
        letters=collections.Counter(magazine)
        for i in ransomNote:
            if i not in letters or letters[i]<=0:
                return False
            letters[i]-=1
        return True
