from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    output=[i,j]
                    return output


solution=Solution()
answer=solution.twoSum([3,3],6)
print(answer)