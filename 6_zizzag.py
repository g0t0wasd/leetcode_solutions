class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        text = [""] * numRows
        index = 0
        direction = 1

        for letter in s:
            text[index] += letter
            index += direction
            if index == numRows - 1 or index == 0:
                direction *= -1

        return "".join(text)
