import os

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
    safe = 0
    for i in input:
        values = [int(x) for x in i.split(" ")]
        temp_safe = True
        # Based on the first index check if the values should decrease or increase
        increaseing = (values[0] - values[1]) < 0
        for index in range(len(values) - 1):
            if not increaseing and 0 < values[index] - values[index + 1] <= 3:
                continue
            elif increaseing and 0 > values[index] - values[index + 1] >= -3:
                continue
            else:
                temp_safe = False
                break
        if temp_safe:
            safe += 1
    return safe


def part_2(input):
    return 0

if __name__ == "__main__":
    if part_1(test_data()) == result_challenge_1():
        print("Challenge 1: Success ! 🥳")
        print(f"Final Solution for Challenge 1: {part_1(input_data())}")
    else:
        print("Challenge 1: Implementation is wrong! 😔")

    if part_2(test_data()) == result_challenge_2():
        print("Challenge 2: Success ! 🥳")
        print(f"Final Solution for Challenge 2: {part_2(input_data())}")
    else:
        print("Challenge 2: Implementation is wrong! 😔")
