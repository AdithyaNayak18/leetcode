class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def atLeastK(k):
            n = len(word)
            vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            has_vowels = set()
            left = ans = consonants = 0

            for right in range(n):
                if word[right] in vowels:
                    vowels[word[right]] += 1
                    has_vowels.add(word[right])
                else:
                    consonants += 1
                
                while len(vowels) == len(has_vowels) and consonants >= k:
                    ans += n - right

                    if word[left] in vowels:
                        vowels[word[left]] -= 1

                        if vowels[word[left]] == 0:
                            has_vowels.remove(word[left])
                    else:
                        consonants -= 1
                    
                    left += 1
                
            return ans
        
        return atLeastK(k) - atLeastK(k + 1)
