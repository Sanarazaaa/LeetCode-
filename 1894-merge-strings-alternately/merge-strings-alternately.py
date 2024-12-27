class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        for i, j in zip(word1, word2):
            merged.append(i)
            merged.append(j)
        merged.extend(word1[len(word2):])
        merged.extend(word2[len(word1):])
        
        return ''.join(merged)

# # word1 = "abcdef"
# word2 = "xy"

# # len(word2) = 2

# # Pairing by zip:
# # 'a-x', 'b-y'

# # Remaining in word1 after 2 characters:
# # word1[2:] = "cdef"

# merged.extend(word1[len(word2):])  # Adds "cdef"
