# from collections import  defaultdict


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        """
            The key ideas behind the solution:
            1. The maximum possible substrings that can end at an index are i + 1.
            2. The contribution of a character to this substring is (i + 1) - it's last seen position.
            3. At each point, sum of all contributions, gives the number of total substrings found so far.
            4. The last seen position of char is actually i + 1.
        """

        # last_position = defaultdict(int) # Used for storing the last position of each character
        # contribution = defaultdict(int) # Used for storing the contribution of each character so far. This
        # will possibly be updated throughout the string traversal
        res = 0

        last_position = {}
        contribution = {}

        for i, char in enumerate(s):
            max_possible_substrs_at_idx = i + 1
            contribution[char] = max_possible_substrs_at_idx - last_position.get(char, 0)
            print(f'{char=} is {contribution=}')

            res += sum(contribution.values())
            last_position[char] = i + 1

        return res


# A

# Input: s = "ABC"
# Output: 10
# Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
# Every substring is composed with only unique letters.
# Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10

if __name__ == '__main__':

    # Example 1
    s = "ABC"
    solution = Solution()
    print(f"s = {s}")
    print(f"uniqueLetterString = {solution.uniqueLetterString(s)}")

    # Example 2
    s = "ABA"
    solution = Solution()
    print(f"s = {s}")
    print(f"uniqueLetterString = {solution.uniqueLetterString(s)}")

    # Example 3
    s = "LEETCODE"
    solution = Solution()
    print(f"s = {s}")
    print(f"uniqueLetterString = {solution.uniqueLetterString(s)}")
