def problem_eleven(filename):
    """
    :param filename: File containing answers to customs form
    :return: Sum of any questions an individual said yes to
    """
    total_sum = 0
    group_answers = set()

    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            if len(line) > 0:
                group_answers |= set(line)
            else:
                total_sum += len(group_answers)
                group_answers = set()

    total_sum += len(group_answers)
    return total_sum


def problem_twelve(filename):
    """
    :param filename: File containing answers to customs form
    :return: Sum of questions every individual member said yes to
    """
    total_sum = 0
    first_set = True
    group_answers = set()

    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            if len(line) > 0:
                individual_answers = set(line)
                if first_set:
                    group_answers = individual_answers
                    first_set = False
                else:
                    group_answers &= individual_answers
            else:
                total_sum += len(group_answers)
                group_answers = set()
                first_set = True

    total_sum += len(group_answers)
    return total_sum


# Test Sets
print(problem_eleven("files/test_custom_forms.txt"))
print(problem_twelve("files/test_custom_forms.txt"))

# Full Set
print(problem_eleven("files/custom_forms.txt"))
print(problem_twelve("files/custom_forms.txt"))
