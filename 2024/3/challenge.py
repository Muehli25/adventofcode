import os
import re

# ------ Read Input ------
path, _ = os.path.split(os.path.abspath(__file__))

def input_data():
    with open(f"{path}/data/input.txt") as file:
        return [i.strip() for i in file.readlines()]


def test_data():
    with open(f"{path}/data/test_1.txt") as file:
        return [i.strip() for i in file.readlines()]


def test_data_2():
    with open(f"{path}/data/test_2.txt") as file:
        return [i.strip() for i in file.readlines()]


def result_challenge_1():
    with open(f"{path}/data/result_test_1.txt") as file:
        return int(file.read())


def result_challenge_2():
    with open(f"{path}/data/result_test_2.txt") as file:
        return int(file.read())

# ------ Helper ------


# ------ Parts ------
def part_1(input):
    result = 0
    for line in input:
        mults = re.findall("mul\\(\\d*,\\d*\\)", line)
        for multiply in mults:
            values = [int(x) for x in re.findall("\\d*", multiply) if x]
            a,b = int(values[0]), int(values[1])
            result += a*b
    return result


def part_2(input):
    result = 0
    mults_on = True
    for line in input:
        do = "do\\(\\)"
        dont = "don't\\(\\)"
        mults = "mul\\((\\d+),(\\d+)\\)"
        for x in re.finditer(f'{do}|{dont}|{mults}', line):
            if re.fullmatch(do, x.group()):
                mults_on = True
            elif re.fullmatch(dont, x.group()):
                mults_on = False
            elif mults_on:
                result += int(x.group(1)) * int(x.group(2))
    return result

if __name__ == "__main__":
    if part_1(test_data()) == result_challenge_1():
        print("Challenge 1: Success ! 🥳")
        print(f"Final Solution for Challenge 1: {part_1(input_data())}")
    else:
        print("Challenge 1: Implementation is wrong! 😔")

    if part_2(test_data_2()) == result_challenge_2():
        print("Challenge 2: Success ! 🥳")
        print(f"Final Solution for Challenge 2: {part_2(input_data())}")
    else:
        print("Challenge 2: Implementation is wrong! 😔")
