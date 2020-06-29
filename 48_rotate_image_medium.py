def rotate(matrix):
    """
    Description:
        You are given an n x n 2D matrix representing an image.
        Rotate the image by 90 degrees (clockwise).
        Note:
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
    Idea:
        Move the elements one by one
    Comlexity:
        Time: O(n**2) - nested loop
        Space: O(1) - in-place
    """
    N = len(matrix) - 1

    # x represents slide from the side of the rectangle to the center
    # In any rectangular matrix there are N // 2 slides till the center
    # In matrixes with odd side we don't need to rotate the number in the middle

    for x in range(N + 1 // 2):
        # In here we iterate over numbers on current slide
        for y in range(x, N-x):
            # Store in temp variable value at the top left of current matrix level
            temp = matrix[x][y]

            # Put in top left position number from bottom left
            matrix[x][y] = matrix[N-y][x]

            # Put in the bottom left number from bottom right
            matrix[N-y][x] = matrix[N-x][N-y]

            # Put in the bottom right number from top right
            matrix[N-x][N-y] = matrix[y][N-x]

            # Put in the top right number from top left
            matrix[y][N-x] = temp

    # Python fun
    # matrix[::] = zip(*matrix[::-1]) clockwise
    # matrix[::] = reversed(list(zip(*matrix[::-1]))) counter-clockwise
