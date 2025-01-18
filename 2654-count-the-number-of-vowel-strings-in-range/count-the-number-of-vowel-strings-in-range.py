class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        vowels = 'aeiou'
        for i in words[left:right+1]:
            if i[0] in vowels and i[-1] in vowels:
                count = count+1
        return count