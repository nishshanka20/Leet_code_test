class Solution:
    def minimumLength(self, s: str) -> int:
        text_dict = {}
        minCount=0
        length=len(s)

        for char in s:
            text_dict[char] = text_dict.get(char, 0) + 1

        print(text_dict)

        for value in text_dict.values():
            if value>=3:
                minCount+=1
        print("mincount",minCount)
        if minCount==0:
            return length
        for value in text_dict.values():
            if value%2==0:
                value2=value-2
            else:
                value2=value-1
            length=length-value2


        return length


solution = Solution()
output=solution.minimumLength(s="aa")
print(output)
