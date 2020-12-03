INPUT = [
    # Pasted from Website
    # List of equal length strings where # indicates a tree
]


def problem_five(input_matrix, slope, tree="#"):
    """
    While ridding a sled through a forest (represented by a map in input_matrix)
    calculate the number of trees that you'll pass using a given slope

    :param input_matrix: A list of strings denoting where trees are located
    :param slope: A tuple of the x, y coordinates
    :param tree: The character that identifies a tree
    :return: The number of trees encountered
    """
    tree_matrix = [[x == tree for x in row] for row in input_matrix]
    row_width = len(tree_matrix[0])

    x_ptr = 0
    y_ptr = 0
    tree_count = 0
    while y_ptr < len(tree_matrix):
        if tree_matrix[y_ptr][x_ptr]:
            tree_count += 1
        x_ptr = (x_ptr + slope[0]) % row_width
        y_ptr += slope[1]

    return tree_count


# First: Find the trees hit with one slope
print(problem_five(INPUT, (3, 1)))
# Second: Find the product of trees hit with 5 different slopes
print(
    problem_five(INPUT, (1, 1))
    * problem_five(INPUT, (3, 1))
    * problem_five(INPUT, (5, 1))
    * problem_five(INPUT, (7, 1))
    * problem_five(INPUT, (1, 2))
)
