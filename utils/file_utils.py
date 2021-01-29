def file_to_list(filename):
    """
    Read file and convert to list of Integer values
    :param filename: One Integer per row
    :return: List of Integers
    """
    with open(filename) as f:
        return [int(line.strip()) for line in f]