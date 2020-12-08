import re
from collections import defaultdict


def build_containment_map(filename):
    """
    Convert a list of bag combinations into a useable map with key: tuple pairs

    Example:
    shiny gold bags contain 2 dark red bags.
    {"shiny gold": [("2", "red bags")]}

    :param filename: Location of bag definitions
    :return: Map of outer bag to inner bags
    """
    containment_map = defaultdict(list)
    with open(filename) as f:
        for line in f:
            line = line.strip()
            vals = [x.strip(", a") for x in re.split(r"bag[s]*", line)]
            for val in vals[1:]:
                val = val.replace("contain ", "")

                if val == ".":
                    break
                elif val == "no other":
                    containment_map[vals[0]] = None
                    break

                s = re.findall(r"\d+|[^\d]+", val)

                bag_count = 0
                bag_color = None
                if s:
                    bag_count = s[0]
                    bag_color = s[1].strip()
                containment_map[vals[0]].append((bag_count, bag_color))

    return containment_map


CONTAINMENT_MAP = build_containment_map("files/bag_containment_rules.txt")
# TEST_MAP = build_containment_map("files/test_bag_containment.txt")


def problem_thirteen(target_bags):
    """
    Calculate how many bags could eventually contain your bag.

    :param target_bags: Which bags are trying to be fit in other bags
    :return: The number of bags that can contain the given bag
    """
    new_bags = set()

    for bag, contents in CONTAINMENT_MAP.items():
        inner_bags = contents and [x[1] for x in contents] or []
        if any([x in inner_bags for x in target_bags]):
            new_bags.add(bag)

    if len(new_bags - target_bags) == 0:
        # Don't include the bag itself in the count
        return len(target_bags) - 1
    else:
        new_target = target_bags | new_bags
        return problem_thirteen(new_target)


def problem_fourteen(main_bag, filename=None, containment_map=None):
    """
    Calculate how many bags your bag could eventually contain

    :param main_bag: The outermost bag
    :return: Sum of bags that can be held (potentially physically impossibly
    within the main bag)
    """
    contained_sum = 0
    for count, inner_bag in CONTAINMENT_MAP[main_bag]:
        if inner_bag in CONTAINMENT_MAP and CONTAINMENT_MAP[inner_bag] is not None:
            inner_sum = problem_fourteen(inner_bag)
            contained_sum += int(count) + int(count) * inner_sum
        else:
            contained_sum += int(count)
    return contained_sum


# print(build_containment_map("files/test_bag_containment.txt"))
# print(problem_fourteen("shiny gold", "files/test_bag_containment.txt"))

print(problem_thirteen(set(["shiny gold"])))
print(problem_fourteen("shiny gold"))
