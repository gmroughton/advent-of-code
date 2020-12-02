import logging

logger = logging.getLogger(__name__)
INPUT = [
    # Pasted from website, list of ints
]


def problem_one(values, target):
    """
    Find two ints in an array that sum to the given target, if found return the
    product of those ints.

    :param values: list of integers
    :param target: the number two ints in values need to sum to
    :return: the product of those two ints if found
    """
    target_map = {}
    for val in values:
        diff = target - val
        if val in target_map:
            return val * diff
        else:
            target_map[diff] = val

    return -1


def problem_two(values, target):
    """
    Find three ints in an array that sum to the given target, if found return the
    product of those ints.

    :param values: list of integers
    :param target: the value three ints in values need to sum to
    :return: the product of those three ints if found
    """
    target_map = {}
    for idx, val in enumerate(values):
        if val in target_map:
            output = val * target_map[val][0] * target_map[val][1]
            return output
        else:
            for x in INPUT[idx+1:]:
                diff = target - (INPUT[idx] + x)
                target_map[diff] = tuple([INPUT[idx], x])

        idx += 1

    return -1


print(problem_one(INPUT, 2020))
print(problem_two(INPUT, 2020))
