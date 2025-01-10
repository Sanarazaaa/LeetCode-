class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        index = word.index(ch) 
        r = []
        r.extend(word[:index + 1][::-1])  # Reverse the prefix
        r.extend(word[index + 1:])
        return ''.join(r) 
