# # find the odd numbers and then count them. return that counted number
# # odd_count = n // 2  # Count of odd numbers before n
# # even_count = (n - 1) // 2  # Count of even numbers before n
#  n = 0
#  m = 0
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         while m <= x:
#              x % 2 == 0:
#             return x //2
# n = 0
# if x% 2 == 0:
#     n = n+1
#     return x//2
#     else:
# #         x// 2 
# # #         m = 0
# # #         while m <=x:
# # #             n = n+1
# # #             m = m +(n*2 + 1)
# # #             return m

# # # #     if n % 2 == 0:  # If n is even
# # #         return n - 1
# # #     else:           # If n is odd
# # #         return n - 2

# class Solution:
#     def mySqrt(self, x: int) -> int:
#         count = 0  # Count of odd numbers
#         m = 0  # Sum of odd numbers

#         # Loop to find the square root
#         while m <= x:
#             count += 1  # Increment count of odd numbers
#             m += (2 * count - 1)  # Add the next odd number (1, 3, 5, ...)

#         return count - 1  # Return the last valid count

class Solution:
    def mySqrt(self, x: int) -> int:
        count = 0  # Count of odd numbers
        m = 0  # Sum of odd numbers

        # Loop to find the square root
        while m <= x:
            count += 1  # Increment count of odd numbers
            m += (2 * count - 1)  # Add the next odd number (1, 3, 5, ...) # to find the series of odd numbers, we use this formula. 

        return count - 1  # Return the last valid count
