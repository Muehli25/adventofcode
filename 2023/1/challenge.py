import string 
import os

path, _ = os.path.split(os.path.abspath(__file__))

def input_data():
    with open(f"{path}/data/input.txt") as file:
        return [i.strip() for i in file.readlines()]


def test_data():
    with open(f"{path}/data/test.txt") as file:
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


def part_1(input):
    result = 0
    for line in input:
        numbers = [i for i in line if i in string.digits]
        result = result + int(numbers[0] + numbers[-1])
    return result


def part_2(input):
    replaced_input = []
    for line in input:
        replaced_input.append(replace_digits(line))
    return part_1(replaced_input)

def replace_digits(input_string):
    line = input_string
    # Sadly there is a overlap in my input, so I need to replace it to allow overlaps
    digits_dict = {"one" :"o1e", "two":"t2o", "three":"t3e", "four":"f4r", "five":"f5e", "six":"s6x", "seven":"s7n", "eight":"e8t", "nine":"n9e"} 
    start = 0
    result_line = line
    while True:
        line = result_line
        for i in range(start, len(line) + 1):
            if line[start:i] in digits_dict.keys():
                result_line = line.replace(line[start:i], digits_dict[line[start:i]])
                break
        start = start + 1
        if start == len(line) + 1: # complete string was replaced.
            return result_line


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
