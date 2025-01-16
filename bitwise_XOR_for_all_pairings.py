from typing import List
from itertools import product


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor_1 = 0
        xor_2=0
        result=0

        for i in (nums1):
            xor_1^=i

        for j in nums2:
            xor_2^=j

        if len(nums1) %2 !=0:
            result^=xor_2

        if len(nums2) %2 !=0:
            result^=xor_1


        return result


solution = Solution()
output = solution.xorAllNums(nums1 = [2,1,3], nums2 = [10,2,5,0])
print(output)
