from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        i=0
        c=[]
        while(i<len(A)):
            j=0
            count=0
            while(j<=i):
                k=0
                while(k<=i):
                    if A[j]==B[k]:
                        count+=1
                    k+=1
                j+=1
            c.append(count)
            i+=1
        return c


solution = Solution()
c = solution.findThePrefixCommonArray(A = [2,3,1], B = [3,1,2])
print(c)

# this complexity is too much. it can be reduce using hashnet. learn it
