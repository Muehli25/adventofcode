import os
import math
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

def check_rule(manual, rule):
    if rule[0] in manual and rule[1] in manual:
        if manual.index(rule[0]) < manual.index(rule[1]):
            return True
        else:
            return False
    return True


# ------ Parts ------
def part_1(input):
    result = 0

    separator = input.index("")
    rules = [x.split("|") for x in input[0:separator]]
    manuals = [x.split(",") for x in input[separator+1:]]

    for manual in manuals:
        correct = True
        for rule in rules:
            if not check_rule(manual, rule):
                correct = False
        if correct:
            result += int(manual[math.floor(len(manual)/2)])
    
    return result

from functools import cmp_to_key

def part_2(input):
    result = 0

    separator = input.index("")
    rules = [x.split("|") for x in input[0:separator]]
    manuals = [x.split(",") for x in input[separator+1:]]

    rules_tuple = [(x.split("|")[0], x.split("|")[1]) for x in input[0:separator]]

    broken_manuals = []

    for manual in manuals:
        correct = True
        for rule in rules:
            if not check_rule(manual, rule):
                correct = False
        if not correct:
            broken_manuals.append(manual)
    
    for manual in broken_manuals:
        manual.sort(
                key=cmp_to_key(
                    lambda lhs, rhs: (
                        -1 if (lhs, rhs) in rules_tuple else (1 if (rhs, lhs) in rules_tuple else 0)
                    )
                )
            )
        result += int(manual[math.floor(len(manual)/2)])

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
