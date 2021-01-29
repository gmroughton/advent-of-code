from collections import defaultdict
from pprint import pprint

from utils.file_utils import file_to_list

TEST_ADAPTERS = file_to_list("files/test_voltage_adapters.txt")
ADAPTERS = file_to_list("files/voltage_adapters.txt")


def problem_ninteen(chain):
    chain.append(0)
    chain.sort()
    chain.append(chain[len(chain) - 1] + 3)
    distribution = defaultdict(int)

    try:
        for idx, val in enumerate(chain):
            diff = chain[idx+1] - val
            distribution[diff] += 1
    except IndexError:
        pass

    pprint(distribution)
    return distribution[1] * distribution[3]


print(problem_ninteen(TEST_ADAPTERS))
print(problem_ninteen(ADAPTERS))
