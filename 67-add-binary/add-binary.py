# bin is used to convert decimal to binary. decimal = 2, binary = 0010
# convert from decimal to binary, use bin. but it introdcues ob in the start, so to remove it, we use [2:] 
# for binary to decimal, use int(a(binary),2(because of binary) )
# Binary to Decimal
# binary = "110"
# decimal_from_binary = int(binary, 2)  # Returns 6
#  Octal to Decimal
# octal = "12"
# decimal_from_octal = int(octal, 8)    # Returns 10

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#                 binary_values= {
#     1: '1',
#     2: '10',
#     3: '11',
#     4: '100',
#     5: '101',
#     6: '110',
#     7: '111',
#     8: '1000',
#     9: '1001',
#     10: '1010'
# }
# for p,v in binary_values.items():
#     if a == v; b == v
#     return a+b
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimal_a = int(a, 2)  # Convert binary strings to decimal integers
        decimal_b = int(b, 2)

        # Add the two decimal integers
        decimal_sum = decimal_a + decimal_b

        # Convert the sum back to binary and remove the '0b' prefix
        return bin(decimal_sum)[2:] # Python bin() function returns the binary string of a given integer.