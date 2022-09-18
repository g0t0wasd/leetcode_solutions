from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        resword, res = '', {''}
        for word in sorted(words):
            if word[:-1] in res:
                res.add(word)
                if len(word) > len(resword):
                    resword = word
        return resword

print(Solution().longestWord(["w","wo","wor","worl","world"]))
print(Solution().longestWord(["a","banana","app","appl","ap","apply","apple"]))
print(Solution().longestWord(["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]))
