from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rules = ('type', 'color', 'name')
        total_count = 0
        index = rules.index(ruleKey)

        for item in items:
            if item[index] == ruleValue:
                total_count += 1

        return total_count


print(Solution().countMatches([["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))
print(Solution().countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"))
