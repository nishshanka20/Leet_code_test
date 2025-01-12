class Solution:
    def canBeValid(self, s, locked):
        # Length of the strings must be even for a valid parentheses string
        if len(s) % 2 != 0:
            return False

        # Left-to-right pass
        open_balance = 0
        flexible_count = 0
        for i in range(len(s)):
            if locked[i] == "0":  # Flexible character
                flexible_count += 1
            elif s[i] == "(":
                open_balance += 1
            elif s[i] == ")":
                if open_balance > 0:
                    open_balance -= 1  # Match a previous '('
                elif flexible_count > 0:
                    flexible_count -= 1  # Use a flexible '('
                else:
                    return False  # Unmatched ')'

        # Right-to-left pass
        close_balance = 0
        flexible_count = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == "0":  # Flexible character
                flexible_count += 1
            elif s[i] == ")":
                close_balance += 1
            elif s[i] == "(":
                if close_balance > 0:
                    close_balance -= 1  # Match a previous ')'
                elif flexible_count > 0:
                    flexible_count -= 1  # Use a flexible ')'
                else:
                    return False  # Unmatched '('

        return True


solution = Solution()
# output = solution.canBeValid(s=")",locked="0")
output = solution.canBeValid(s="((()(()()))()((()()))))()((()(()"
,locked="10111100100101001110100010001001")
print(output)
