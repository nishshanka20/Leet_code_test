from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original=[0]
        for i in range(len(derived)):
            if derived[i]==1:
                if i<len(derived)-1:
                    if original[i]==0:
                        original.append(1)
                    else:
                        original.append(0)
                else:
                    if original[i]==0:
                        if original[0]==1:
                            return True
                        else:
                            return False
                    else:
                        if original[0]==0:
                            return True
                        else:
                            return False
            else:
                if i<len(derived)-1:
                    if original[i]==0:
                        original.append(0)
                    else:
                        original.append(1)
                else:
                    if original[i]==0:
                        if original[0]==0:
                            return True
                        else:
                            return False
                    else:
                        if original[0]==1:
                            return True
                        else:
                            return False




solution = Solution()
answer = solution.doesValidArrayExist(derived = [1,0])
print(answer)
