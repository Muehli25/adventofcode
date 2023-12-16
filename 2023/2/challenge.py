import os

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


def part_1(input):
    max_red = 12
    max_green = 13
    max_blue = 14

    result = 0
    for line in input:
        game_number, red, green, blue = parse_data(line)
        if red <= max_red and green <= max_green and blue <= max_blue:
            result = result + game_number
    return result

def part_2(input):
    result = 0
    for line in input:
        _, red, green, blue = parse_data(line)
        result = result + (red*green*blue)
    return result

def parse_data(line):
    game_number = int(line.split(":")[0].split(" ")[1])
    rounds = line.split(":")[1].split(";")
    red, green, blue = 0,0,0
    for round in rounds:
        cubes = round.split(",")
        for cube in cubes:
            cube = cube.strip()
            if "red" in cube:
                red = max(int(cube.split(" ")[0]), red)
            if "green" in cube:
                green =  max(int(cube.split(" ")[0]), green)
            if "blue" in cube:
                blue = max(int(cube.split(" ")[0]), blue)

    return game_number, red, green, blue


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
