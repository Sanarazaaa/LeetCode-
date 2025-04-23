class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_n = 0
        prod_n = 1
        original_n = n
        while n >0:
            digit = n%10
            sum_n +=digit
            prod_n *=digit
            n = n//10
        return prod_n - sum_n


# in this code, in the first while, n is getting. so when it reaches the second loop, n will be changed.

#         sum_n = 0
#         prod_n = 1
#         while n > 0:
#             digit = n % 10
#             sum_n += digit
#             n = n//10
#     #    return sum_n 
#         while n > 0:
#             digit = n % 10
#             prod_n *= digit
#             n = n//10
#    #     return prod_n
         