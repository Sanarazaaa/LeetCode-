class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        map_char_to_word = {}
        map_word_to_char = {}

        for char, word in zip(pattern, words):
            if char in map_char_to_word:
                if map_char_to_word[char] != word:
                    return False
            else:
                if word in map_word_to_char:
                    return False
                map_char_to_word[char] = word
                map_word_to_char[word] = char

        return True
