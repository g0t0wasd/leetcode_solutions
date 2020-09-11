class Solution:
    """
    Description:
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
        Note: You may not slant the container and n is at least 2.
        The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
        Example:

        Input: [1,8,6,2,5,4,8,3,7]
        Output: 49
    Idea:
        Take the entries from different size and compare it's resulted area
    Complexity:
        Time: O(n) size of an array
        Space: O(1)
    """
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        res = 0
        while left_index < right_index:
            left_number = height[left_index]
            right_number = height[right_index]
            area = min(left_number, right_number) * (right_index - left_index)
            if area > res:
                res = area
            if left_number < right_number:
                left_index += 1
            else:
                right_index -= 1
        return res
