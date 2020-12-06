def problem_eleven(filename):
    """
    :param filename: File containing answers to customs form
    :return: Sum of any yes for each group
    """
    total_sum = 0
    unique_yes = set()
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            if len(line) == 0:
                total_sum += len(unique_yes)
                unique_yes = set()
            else:
                unique_yes |= set(line)

    total_sum += len(unique_yes)
    return total_sum


def problem_twelve(filename):
    """
    :param filename: File containing answers to customs form
    :return: Sum of questions all members sed yes to
    """
    total_sum = 0
    every_yes = set()
    first_set = True
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            if len(line) == 0:
                total_sum += len(every_yes)
                every_yes = set()
                first_set = True
            else:
                line_yes = set(line)
                if first_set:
                    every_yes = line_yes
                    first_set = False
                else:
                    every_yes &= line_yes

    total_sum += len(every_yes)
    return total_sum


# Test Sets
print(problem_eleven("files/small_custom_forms.txt"))
print(problem_twelve("files/small_custom_forms.txt"))

# Full Set
print(problem_eleven("files/custom_forms.txt"))
print(problem_twelve("files/custom_forms.txt"))
