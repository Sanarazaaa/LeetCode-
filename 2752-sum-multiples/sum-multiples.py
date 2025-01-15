# class Solution:
#     def sumOfMultiples(self, n: int) -> int:
#         total_sum = 0  # Initialize the sum
#         for num in range(1, n+1):
#             # Check if the number is divisible by 3, 5, or 7
#             if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
#                 total_sum += num  # Add the number to the sum
#         return total_sum

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        
        def sumOfMultiplesOf(k):
            return k*(n//k)*(n//k+1)//2

        return ( sumOfMultiplesOf(3) + sumOfMultiplesOf(5) + sumOfMultiplesOf(7)  
                    - sumOfMultiplesOf(15) - sumOfMultiplesOf(21) - sumOfMultiplesOf(35) 
                    + sumOfMultiplesOf(105) )
        


# just using this is incorrect because  num is a single number, and sum() should be used to sum a list of numbers.
# range(1, n) will iterate from 1 to n-1, but it will not include n
# to include n, we need to use n+1