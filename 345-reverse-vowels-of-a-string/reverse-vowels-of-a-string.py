class Solution:
    def reverseVowels(self, s: str) -> str:
        v = 'aeiouAEIOU'
        v_s = ''
        for i in s:
            if i in v:
                v_s += i
        p = len(v_s) - 1
        ss = list(s)
        for i in range(len(s)):
            if s[i] in v:
                ss[i] = v_s[p]
                p -= 1
        return ''.join(ss)