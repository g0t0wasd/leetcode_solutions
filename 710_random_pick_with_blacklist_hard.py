from random import randint


class Solution:
    def __init__(self, N, blacklist):
        blacklist = sorted(blacklist)
        self.b = set(blacklist)
        self.m = {}
        self.length = N - len(self.b)
        j = 0
        for i in range(self.length, N):
            if i not in self.b:
                self.m[blacklist[j]] = i
                j += 1

    def pick(self):
        num = randint(0, self.length - 1)
        return self.m.get(num, num)


print(Solution(7, [2, 3, 6]).pick())
print(Solution(4, [2, 1]).pick())
