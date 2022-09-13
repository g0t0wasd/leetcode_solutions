class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)

        upper, lower = ord('Z'), ord('z')

        for i in range(26):
            cap_case = chr(upper - i)
            low_case = chr(lower - i)
            if cap_case in s and low_case in s:
                return cap_case

        return ''


print(Solution().greatestLetter("lEeTcOdE"))
print(Solution().greatestLetter("arRAzFif"))
print(Solution().greatestLetter("AbCdEfGhIjK"))
