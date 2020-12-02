PASSWORDS = [
    # Pasted from Website / converted to a list of tuples
    #     # ("1-2 a", "aanvddda")
]


def problem_three(values):
    """
    Validate a list of passwords based on the corporate policy at the time.

    Corporate Policy:
    (1-2 a) = The character 'a' needs to occur at list 1 but not more than two
    times in the password

    :param values: a list of tuples that each contain a policy and password
    :return: the number of valid passwords in <values>
    """
    valid = 0
    for policy, value in values:
        valid_range, character = policy.split(" ")
        lower, upper = valid_range.split("-")

        if int(lower) <= value.count(character) <= int(upper):
            valid += 1

    return valid


def problem_four(values):
    """
    Validate a list of passwords based on the corporate policy at the time.

    Corporate Policy:
    (1-2 a) = The character 'a' needs to exist in either the first or second
    position of the password but not both

    :param values: a list of tuples that each contain a policy and password
    :return: the number of valid passwords in <values>
    """
    valid = 0
    for policy, value in values:
        valid_range, character = policy.split(" ")
        lower, upper = valid_range.split("-")

        if (value[int(lower)-1] == character) != (value[int(upper)-1] == character):
            valid += 1

    return valid


print(problem_three(PASSWORDS))
print(problem_four(PASSWORDS))
