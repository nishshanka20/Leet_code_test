# class Solution:
#     def minimizeXor(self, num1: int, num2: int) -> int:
#         num2_bin = bin(num2)
#         num1_bin = bin(num1)
#         num1_bin = num1_bin[2:]
#         len_for_x = max(len(num1_bin),len(num2_bin))
#
#         count1=bin(num2).count('1')
#
#         maxvalue = 2 ** len_for_x
#
#         min_val = maxvalue-1
#         min_num=0
#
#         for i in range(num1,maxvalue):
#             counts=bin(i).count('1')
#             if counts == count1:
#
#                 if i ^ num1 < min_val:
#                     min_val= i ^ num1
#                     min_num=i
#
#         return min_num
#
#
# solution = Solution()
# output = solution.minimizeXor(num1 = 3, num2 = 5)
# print("solution", output)
# class Solution:
#     def minimizeXor(self, num1: int, num2: int) -> int:
#         num2_bin = bin(num2)
#         num1_bin = bin(num1)
#         num1_bin = num1_bin[2:]
#         len_for_x = max(len(num1_bin),len(num2_bin))
#
#         count1=bin(num2).count('1')
#         value="ob"
#         for i in range(30):
#             for j in range (len(num1_bin)):
#                 if num1_bin[j]=="1":
#                     if count1>0:
#                         count1-=1
#                         value=value+"1"
#                     else:
#                         value=value+"0"
#             if count1>0:
#                 value="1"+value
#
#
#
#         return 0

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count1 = bin(num2).count('1')

        x = 0

        for i in range(31, -1, -1):
            if num1 & (1 << i):
                if count1 > 0:
                    x |= (1 << i)
                    count1 -= 1

        for i in range(32):
            if count1 == 0:
                break
            if not (x & (1 << i)):
                x |= (1 << i)
                count1 -= 1

        return x


# Example usage
solution = Solution()
output = solution.minimizeXor(num1=3, num2=5)
print("solution:", output)



# solution = Solution()
# output = solution.minimizeXor(num1 = 3, num2 = 5)
# print("solution", output)
