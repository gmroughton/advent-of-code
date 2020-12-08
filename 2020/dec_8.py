import copy
from pprint import pprint


def program_to_list(filename):
    """
    Convert a file into a list representing commands in an assembly-like language

    :param filename: File containing instruction set
    :return: The program loaded into memory as a list of instructions
    """
    output = []
    with open(filename) as f:
        for line in f:
            vals = line.split()
            output.append([vals[0], int(vals[1].strip('+'))])

    return output


TEST_PROGRAM = program_to_list("files/test_infinite_program.txt")
FULL_PROGRAM = program_to_list("files/infinite_program.txt")


def run_program(program):
    """
    Run a program and return the current acc value and a boolean representing
    whether or not it fully completed or ran into an infinit loop

    :param program: List of instructions
    :return: Sum, True if runs to end of instruction set, False otherwise
    """
    global_sum = 0
    line_ptr = 0
    repeat_lines = []
    while True:
        if line_ptr in repeat_lines:
            return global_sum, False
        elif line_ptr > len(program) - 1:
            return global_sum, True

        instruction, value = program[line_ptr]
        repeat_lines.append(line_ptr)
        if instruction == "acc":
            global_sum += value
            line_ptr += 1
        elif instruction == "nop":
            line_ptr += 1
        elif instruction == "jmp":
            line_ptr += value


def problem_fifteen():
    """
    Run the program as is and return the acc when the first loop is encountered

    :return: Value of accumulator on program termination
    """
    return run_program(FULL_PROGRAM)[0]


def problem_sixteen():
    """
    Run the program, but change one nop / jmp at a time to see if it results in
    a new instruction set that allows the program to complete normally.

    :return: Value of accumulator for instruction set that successfully runs
    """
    program = FULL_PROGRAM

    line_ptr = 0
    while True:
        instruction, value = program[line_ptr]
        if instruction == "acc":
            line_ptr += 1
        elif instruction == "nop":
            new_program = copy.deepcopy(program)
            new_program[line_ptr][0] = "jmp"
            final_sum, completed = run_program(new_program)
            if completed:
                return final_sum
            line_ptr += 1
        elif instruction == "jmp":
            new_program = copy.deepcopy(program)
            new_program[line_ptr][0] = "nop"
            final_sum, completed = run_program(new_program)
            if completed:
                return final_sum
            line_ptr += value


print(f"FIFTEEN: {problem_fifteen()}")
print(f"SIXTEEN: {problem_sixteen()}")