import yaml
import re


def str_to_dict(string):
    """
    Convert a raw text string into valid YAML and then load it

    :param string: Key value pairs (e.g. "key:value key_2:value_2")
    :return: dict
    """
    string = string.replace(" ", "\n").replace(":", ": ").replace("#", "\\#")
    return yaml.load(string, Loader=yaml.BaseLoader)


def validate_passport(passport):
    """
    Given a passport dictionary, validate based on give criteria

    :param passport: dict
    :return: True if valid, False if not
    """
    for key, val in passport.items():
        if key == "byr":
            # Birth Year
            if not (1920 <= int(val) <= 2002):
                return False
        elif key == "iyr":
            # Issue Year
            if not (2010 <= int(val) <= 2020):
                return False
        elif key == "eyr":
            # Expiration Year
            if not (2020 <= int(val) <= 2030):
                return False
        elif key == "hgt":
            # Height
            if "cm" in val:
                number = int(val.rstrip("cm"))
                if not (150 <= number <= 193):
                    return False
            elif "in" in val:
                number = int(val.rstrip("in"))
                if not (59 <= number <= 76):
                    return False
            else:
                return False
        elif key == "hcl":
            # Hair Color
            if not re.match(r"\\#[0-9a-f]{6}", val):
                return False
        elif key == "ecl":
            # Eye Color
            valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if val not in valid_eye_colors:
                return False
        elif key == "pid":
            # Passport ID
            if not re.match(r"\d{9}", val):
                return False
    return True


def problem_seven(filename, validate=False):
    """
    Based on a list of key:value pairs determine if passports are valid, first
    by checking that they have all fields, then by validating the individual
    fields for correctness.

    :param filename: File with passport data
    :return: Count of number of valid passports
    """
    required_fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    current_passport = ""
    valid = 0

    with open(filename) as f:

        for line in f:
            if line == "\n":
                if all([x in current_passport for x in required_fields]):
                    if not validate:
                        valid += 1
                    elif validate_passport(str_to_dict(current_passport)):
                        valid += 1
                current_passport = ""
            else:
                current_passport += line.replace("\n", " ")

    return valid


# Problem 7: Check that required fields exist
print(problem_seven("files/passports.txt"))
# Problem 8: Validate the data in each field
print(problem_seven("files/passports.txt", validate=True))
