def pass_to_seat(line):
    """
    Convert a boarding pass string to an integer seat id

    Example Boarding Pass
    FBFBBFFRLR == Row: 44 Col: 5

    :param line: String representing a seat id
    :return: Integer seat id
    """
    row = int(line[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(line[7:10].replace("L", "0").replace("R", "1"), 2)
    return (row * 8) + col


def problem_nine(filename):
    """
    Find the highest seat_id to validate the binary space patitioning -> seat id
    algorithm

    :param filename: List of boarding passes
    :return: Highest Seat ID
    """
    with open(filename) as f:
        seat_ids = [pass_to_seat(line) for line in f]
    return max(seat_ids)


def problem_ten(filename):
    """
    Find the missing seat id from a list boarding passes of a fully boarded
    plane

    :param filename: List of boarding passes
    :return: Missing Seat ID (your seat)
    """
    with open(filename) as f:
        seat_ids = [pass_to_seat(line) for line in f]

    seat_ids.sort()
    idx = 0
    while idx < len(seat_ids):
        if seat_ids[idx] + 1 != seat_ids[idx + 1]:
            return seat_ids[idx] + 1
        idx += 1


print(problem_nine("files/boarding_passes.txt"))
print(problem_ten("files/boarding_passes.txt"))
