def load_cypher(filename):
    """
    Read file and convert to list of Integer values
    :param filename: One Integer per row
    :return: List of Integers
    """
    with open(filename) as f:
        return [int(line.strip()) for line in f]


TEST_CYPHER = load_cypher("files/test_xmas_cypher.txt")
CYPHER = load_cypher("files/xmas_cypher.txt")


def two_number_sum(array, target_sum):
    """
    Find if there are two values in an array that sum to the target value

    :param array: List of Integers
    :param target_sum: integer target value
    :return: True if Found, False if Not
    """
    ptr = 0
    while ptr < len(array) - 1:
        a = array[ptr]
        for x in array[ptr:]:
            if a + x == target_sum:
                return True
        ptr += 1
    return False


def problem_seventeen(cypher, window):
    """
    Find the first value in the cypher that can't be summed with a pair of values
    in the trailing <window> number of values in the cypher

    :param cypher: List of Integers
    :param window: Size of window in which to search for pairs to sum
    :return: First number that can't be summed
    """

    window_left = 0
    window_right = window
    test_value = cypher[window]
    while two_number_sum(cypher[window_left:window_right], test_value):
        window_left += 1
        window_right += 1
        test_value = cypher[window_right]

    return test_value


def problem_eighteen(cypher, window):
    """
    Find a contiguous group of ints in the cypher that add to the value found
    in problem seventeen. Output the sum of the min and max values in that group.

    :param cypher: List of Integers
    :param window: Size of window in which to search for pairs to sum
    :return: Sum of min and max in the group that meets the reqs
    """
    target = problem_seventeen(cypher, window)

    start_val = 0
    moving_ptr = 0
    contiguous_sum = 0
    while start_val < cypher.index(target) - 1:
        contiguous_sum += cypher[moving_ptr]

        if contiguous_sum == target:
            sum_range = cypher[start_val + 1: moving_ptr + 1]
            return min(sum_range) + max(sum_range)
        elif contiguous_sum > target:
            contiguous_sum = 0
            start_val += 1
            moving_ptr = start_val

        moving_ptr += 1

    return False


print(problem_seventeen(TEST_CYPHER, 5))
print(problem_seventeen(CYPHER, 25))

print(problem_eighteen(TEST_CYPHER, 5))
print(problem_eighteen(CYPHER, 25))
