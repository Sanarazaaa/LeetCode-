class Solution:
    def findComplement(self, num: int) -> int:
        binary = format(num, 'b')
        rev = ''.join('1' if bit == '0' else '0' for bit in binary)
        decimal = int(rev, 2)
        return decimal
