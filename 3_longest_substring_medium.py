def len_max_subst_wo_reps(text):
    """
    Description:
        Given a string, find the length of the longest substring without repeating characters.
    Idea:
        Create sliding window with the start point at start. Write the letters to the
        HashTable to reinitialize the start point in case of duplicate letter
    Complexity:
        Time: O(n). We only once iterate over the text
        Space: O(n). HashTable to store the seen results
    """
    seen = {}
    max_len = 0
    start = 0
    for i, ch in enumerate(text):
        if ch in seen and start <= seen[c]:
            start = seen[c] + 1
        else:
            max_len = max(max_len, i - start + 1)
        seen[c] = i
    return max_len
