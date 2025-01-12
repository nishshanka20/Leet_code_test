class Solution(object):
    def canConstruct(self, s, k):
        if (len(s) < k):
            return False

        text_dict = {}

        for char in s:
            text_dict[char] = text_dict.get(char, 0) + 1

        print(text_dict)
        count=0
        for value in text_dict.values():
            if value %2 !=0:
                count+=1

        if count>k:
            return False
        else:
            return True


solution = Solution()
answer=solution.canConstruct(s = "true", k = 4)
print(answer)
